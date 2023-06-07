import sys
import token

sys.path.append('../')

import os
import json
from data import DATA_DIR
from datasets import load_dataset
import random
import tiktoken
from templates import TEMPLATES
import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Generate swiss_legal_data test sets.')
    parser.add_argument("--config_name", type=str,
                        default=None, help="Name of config.")
    parser.add_argument("--number_of_samples", type=int,
                        default=2000, help="Number of samples")

    args = parser.parse_args()

    if args.config_name is None:
        configs = [
            "swiss_criticality_prediction_bge_considerations",
            "swiss_criticality_prediction_bge_facts",
            "swiss_criticality_prediction_citation_considerations",
            "swiss_criticality_prediction_citation_facts",
            "swiss_judgment_prediction_xl_considerations",
            "swiss_judgment_prediction_xl_facts",
            "swiss_law_area_prediction_facts",
            "swiss_law_area_prediction_considerations",
            "swiss_law_area_prediction_sub_area_considerations",
            "swiss_law_area_prediction_sub_area_facts"
        ]
    elif ',' in args.config_name:
        configs = args.config_name.split(',')
        configs = [conf.strip() for conf in configs]
    else:
        configs = [args.config_name]
    entire_costs = 0

    for config_name in configs:
        print('+++ Processing config ', config_name, '+++')
        # Load test dataset and labels
        dataset = load_dataset("joelito/lextreme", config_name,
                               use_auth_token='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')
        validation_dataset = dataset['validation']
        validation_dataset = validation_dataset.filter(lambda x: len(x['input']) > 0)
        if args.number_of_samples <= validation_dataset.num_rows:
            number_of_samples = args.number_of_samples
        else:
            number_of_samples = validation_dataset.num_rows
        label_names = validation_dataset.features['label'].names

        random.seed(42)
        random_ids = random.sample(range(len(validation_dataset)), k=number_of_samples)
        validation_dataset = validation_dataset.select(random_ids)

        # Compute templated text tokens
        templated_text = TEMPLATES[config_name]['INPUT_INTRODUCTORY_TEXT'] + '\n" "\n\n'
        templated_text += TEMPLATES[config_name]['OPTIONS_PRESENTATION_TEXT']
        for end_idx, label_name in enumerate(label_names):
            templated_text += f'- {label_name}\n'
        templated_text += TEMPLATES[config_name]['QUESTION_TEXT']

        tokenizer = tiktoken.encoding_for_model("gpt-3.5-turbo")
        templated_text_length = len(tokenizer.encode(templated_text))

        total_input = ''
        with open(os.path.join(DATA_DIR, 'instruction-following-examples', config_name + '.jsonl'),
                  'w') as file:
            for idx, sample in enumerate(validation_dataset):
                text = sample["input"]
                language = sample["language"]
                words = text.split(' ')
                for threshold in [4000, 3800, 3600, 3400, 3200, 3000, 2800, 2600, 2400, 2000, 1000, 500]:
                    shortened_text = ' '.join(words[:threshold])
                    input_text_length = len(tokenizer.encode(shortened_text))
                    if templated_text_length + input_text_length <= 3900:
                        break

                text_input = TEMPLATES[config_name]['INPUT_INTRODUCTORY_TEXT'] + \
                                f'\n"{shortened_text}"\n\n'
                text_input += TEMPLATES[config_name]['OPTIONS_PRESENTATION_TEXT']
                for end_idx, label_name in enumerate(label_names):
                    text_input += f'-  {label_name}\n'
                text_input += TEMPLATES[config_name]['QUESTION_TEXT']
                # print(text_input)
                answer = label_names[sample['label']]
                label = sample['label']

                file.write(json.dumps(
                    {'input_text': text_input, 'language': language, 'answer': answer, 'label': label,
                        'input': sample['input'], 'input_text_length': input_text_length},
                    ensure_ascii=False) + '\n')
                # print(f"{TEMPLATES[config_name]['QUESTION_TEXT']} {answer}")
                # print('-' * 100)
                total_input += text_input
                        

        # Count tokens and cost
        tokenizer = tiktoken.encoding_for_model("gpt-3.5-turbo")
        total_n_tokens = len(tokenizer.encode(total_input)) + 100 * 1000
        entire_costs += total_n_tokens
        print(f'The total number of tokens is {total_n_tokens}, with an '
              f'estimated processing cost of {total_n_tokens * (0.002 / 1000):.2f}$.')
    print('Entire costs that probably will be spend: ', f'estimated processing cost of {entire_costs * (0.002 / 1000):.2f}$.')
