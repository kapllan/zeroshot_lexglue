import json
import os.path
import random
import tqdm
from handle_llama_model import get_llama_pipeline
from handle_claude_model import anthropic
import argparse
from data import DATA_DIR
from build_instructions.templates import TEMPLATES
from constants import *
from anthropic import Anthropic, HUMAN_PROMPT, AI_PROMPT

random.seed(42)

LIMIT = 10


def get_prediction(input: str, model_name: str, model) -> str:
    if 'llama' in model_name:
        response = model(example['input_text'])


def main(args):
    if 'llama' in args.model_name:
        model = get_llama_pipeline()
    elif args.model_name == 'claude-2':
        model = anthropic

    OPTIONS_PRESENTATION_TEXT = TEMPLATES[args.dataset_name]['OPTIONS_PRESENTATION_TEXT']
    QUESTION_TEXT = TEMPLATES[args.dataset_name]['QUESTION_TEXT']
    dataset = []
    label_wise_dataset = {}

    with open(os.path.join(DATA_DIR + '/instruction-following-examples/', f'{args.dataset_name}.jsonl')) as in_file:
        for line in in_file:
            sample_data = json.loads(line)
            dataset.append(sample_data)

    predictions = []
    '''if os.path.exists(os.path.join(DATA_DIR + f'/{args.zeroshot_output_path}/',
                                   f'{args.dataset_name}_{args.model_name}_predictions.jsonl')):
        with open(os.path.join(DATA_DIR + f'/{args.zeroshot_output_path}/',
                               f'{args.dataset_name}_{args.model_name}_predictions.jsonl')) as in_file:
            for line in in_file:
                predictions.append(json.loads(line))'''

    # dataset = dataset[:LIMIT]
    # predictions = predictions[:LIMIT]
    for idx, example in tqdm.tqdm(enumerate(dataset)):
        if len(predictions) and predictions[idx]['prediction'] is not None:
            dataset[idx]['prediction'] = predictions[idx]['prediction']
            print(f'Predictions for example #{idx} is already available!')
            continue
        if args.model_name == 'llama':
            try:
                if 'llama' in args.model_name:
                    response = model(example['input_text'])[0]["generated_text"]
                elif args.model_name == 'claude-2':
                    response = anthropic.completions.create(
                        model="claude-2",
                        max_tokens_to_sample=MAX_OUTPUT_LENGTH,
                        prompt=f"{HUMAN_PROMPT} {example['input_text']}{AI_PROMPT}",
                    ).completion
                dataset[idx]['prediction'] = response
            except Exception as inst:
                print(inst)
                dataset[idx]['prediction'] = None

    folder_name = args.zeroshot_output_path
    main_output_dir = os.path.join(DATA_DIR, folder_name)
    if not os.path.exists(main_output_dir):
        os.mkdir(main_output_dir)
    with open(os.path.join(main_output_dir,
                           f'{args.dataset_name}_{args.model_name}_predictions.jsonl'), 'w') as file:
        for example in dataset:
            file.write(json.dumps(example, ensure_ascii=False) + '\n')


parser = argparse.ArgumentParser(description='Prompting GPT')
parser.add_argument("--dataset_name", type=str,
                    default='ledgar', help="Name of dataset as stored on HF")
parser.add_argument("--truncate_demonstrations", type=int,
                    default=100, help="Truncation of demonstrations")
parser.add_argument("--zeroshot_output_path", help="Define the zero shot putput directory.",
                    default="llama_zero-shot-predictions")
parser.add_argument("--model_name", type=str, help="model name")

args = parser.parse_args()

main(args)
