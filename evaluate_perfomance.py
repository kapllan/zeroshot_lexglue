import json
import re

import numpy as np
import os
from sklearn.metrics import classification_report
from datasets import load_dataset
from data import DATA_DIR
import argparse
from sentence_transformers import SentenceTransformer, util
import pandas as pd
from ast import literal_eval

model = SentenceTransformer('clips/mfaq')  #all-MiniLM-L6-v2: We needed a multi-lingual model

EUROVOC_CONCEPTS = ['political framework', 'politics and public safety', 'executive power and public service',
                    'international affairs', 'cooperation policy', 'international security', 'defence',
                    'EU institutions and European civil service', 'European Union law', 'European construction',
                    'EU finance', 'civil law', 'criminal law', 'international law', 'rights and freedoms',
                    'economic policy',
                    'economic conditions', 'regions and regional policy', 'national accounts', 'economic analysis',
                    'trade policy', 'tariff policy', 'trade', 'international trade', 'consumption', 'marketing',
                    'distributive trades', 'monetary relations', 'monetary economics',
                    'financial institutions and credit',
                    'free movement of capital', 'financing and investment', 'public finance and budget policy',
                    'budget',
                    'taxation', 'prices', 'social affairs', 'social protection', 'health', 'documentation',
                    'communications',
                    'information and information processing', 'information technology and data processing',
                    'natural and applied sciences', 'business organisation', 'business classification', 'management',
                    'accounting', 'competition', 'employment', 'labour market',
                    'organisation of work and working conditions', 'personnel management and staff remuneration',
                    'transport policy', 'organisation of transport', 'land transport',
                    'maritime and inland waterway transport', 'air and space transport', 'environmental policy',
                    'natural environment', 'deterioration of the environment', 'agricultural policy',
                    'agricultural structures and production', 'farming systems', 'cultivation of agricultural land',
                    'means of agricultural production', 'agricultural activity', 'fisheries', 'plant product',
                    'animal product', 'processed agricultural produce', 'beverages and sugar', 'foodstuff',
                    'agri-foodstuffs', 'food technology', 'production', 'technology and technical regulations',
                    'research and intellectual property', 'energy policy', 'coal and mining industries', 'oil industry',
                    'electrical and nuclear industries', 'industrial structures and policy', 'chemistry',
                    'iron, steel and other metal industries', 'mechanical engineering',
                    'electronics and electrical engineering', 'building and public works', 'wood industry',
                    'leather and textile industries', 'miscellaneous industries', 'Europe',
                    'regions of EU Member States',
                    'America', 'Africa', 'Asia and Oceania', 'economic geography', 'political geography',
                    'overseas countries and territories', 'United Nations']

SCOTUS_AREAS = ['Criminal Procedure', 'Civil Rights', 'First Amendment', 'Due Process', 'Privacy', 'Attorneys',
                'Unions', 'Economic Activity', 'Judicial Power', 'Federalism', 'Interstate Relations',
                'Federal Taxation', 'Miscellaneous']

swiss_legal_data_configs = [
            "swiss_criticality_prediction_bge_considerations",
            "swiss_criticality_prediction_bge_facts",
            "swiss_criticality_prediction_citation_considerations",
            "swiss_criticality_prediction_citation_facts",
            "swiss_judgment_prediction_xl_considerations",
            "swiss_judgment_prediction_xl_facts",
            "swiss_law_area_prediction_facts",
            "swiss_law_area_prediction_considerations",
            "swiss_law_area_prediction_sub_area_considerations",
            "swiss_law_area_prediction_sub_area_facts",
            "brazilian_court_decisions_judgment",
            "brazilian_court_decisions_unanimity",
            "german_argument_mining",
            "greek_legal_code_chapter",
            "greek_legal_code_subject",
            "greek_legal_code_volume",
            "swiss_judgment_prediction",
            "online_terms_of_service_unfairness_levels",
            "online_terms_of_service_clause_topics",
            "covid19_emergency_event",
            "multi_eurlex_level_1",
            "multi_eurlex_level_2",
            "multi_eurlex_level_3",
            # "greek_legal_ner",
            # "legalnero",
            # "lener_br",
            # "mapa_coarse",
            # "mapa_fine"
]

def make_boolean(value):
    value_capitalized = str(value).lower().title()
    if literal_eval(value_capitalized) in [True, False, None]:
        return literal_eval(str(value).title())
    else:
        return value

def main(args):
    if args.dataset_name in swiss_legal_data_configs:
        benchmark = "joelito/lextreme"
        split = "validation"
    else:
        benchmark = "lexlms/lex_glue_v2"
        split = "test"
    predict_dataset = load_dataset(benchmark, args.dataset_name, split=split)

    multi_label = make_boolean(args.multi_label)

    if multi_label:
        if args.dataset_name != 'eurlex':
            label_names = [f'{label_name}'.lower() for idx, label_name in
                           enumerate(predict_dataset.features['label'].feature.names)] + ['none']
        else:
            label_names = ['Article ' + label.lower() for label in EUROVOC_CONCEPTS]
    else:
        if args.dataset_name != 'scotus':
            label_names = [f'{label_name}'.lower() for idx, label_name in
                           enumerate(predict_dataset.features['label'].names)]

        else:
            label_names = [label.lower() for label in SCOTUS_AREAS]

    label_names = sorted(label_names, key=lambda x: len(x), reverse=True)


    label_embeddings = [model.encode(label) for label in label_names]
    dataset = []
    name_extension = f'_few_shot-{args.few_shot_k}' if args.few_shot_k else ''
    folder_name = f'_few_shot-predictions' if args.few_shot_k else 'zero-shot-predictions'
    with open(os.path.join(DATA_DIR, folder_name,
                           f'{args.dataset_name}_{args.model_name}_predictions{name_extension}.jsonl')) as file:
        for line in file:
            dataset.append(json.loads(line))
    print('Number of examples: ', len(dataset))
    noisy_labels = 0
    labels = np.zeros((len(dataset), len(label_names)))
    predictions = np.zeros((len(dataset), len(label_names)))
    nones = 0
    for idx, example in enumerate(dataset):
        if example['prediction'] is not None:
            for l_idx, label_name in enumerate(label_names):
                if not multi_label:
                    if sum(labels[idx]) == 0:
                        if label_name in dataset[idx]['answer'].lower():
                            labels[idx][l_idx] = 1
                    if sum(predictions[idx]) == 0:
                        if label_name in example['prediction'].lower():
                            predictions[idx][l_idx] = 1
                else:
                    if label_name in dataset[idx]['answer'].lower():
                        labels[idx][l_idx] = 1
                    if label_name in example['prediction'].lower():
                        predictions[idx][l_idx] = 1
            if sum(predictions[idx]) == 0:
                if multi_label:
                    preds = [pred.strip('.').strip(' ').strip('\n') for pred in
                             re.split('[\n,]', example['prediction'].lower())]
                else:
                    preds = [example['prediction'].lower()]
                for pred in preds:
                    if len(pred) >= 3:
                        pred_embeddings = model.encode(pred)
                        label_id = util.cos_sim(pred_embeddings, label_embeddings).argmax().numpy()
                        predictions[idx][label_id] = 1
                        # print(f'Prediction "{pred}" best matches label "{dataset[idx]["answer"].lower()}"')
                noisy_labels += 1
        else:
            print('Not prediced: ', example['prediction'])
            nones += 1

    print(f'{nones} question unanswered!\n')
    print(f'{noisy_labels} noisy answers!\n')
    print(classification_report(y_true=labels, y_pred=predictions, target_names=label_names, zero_division=0, digits=3))
    report = classification_report(y_true=labels, y_pred=predictions, target_names=label_names, zero_division=0,
                                   digits=3, output_dict=True)
    report_df = pd.DataFrame(report)
    report_df["metric"] = report_df.index
    report_df['finetuning_task'] = args.dataset_name
    report_df['question unanswered'] = nones
    report_df['noisy answers'] = noisy_labels
    if not os.path.exists('reports/'):
        os.makedirs('reports')

    report_df.to_excel('reports/evaluation_report_' + args.dataset_name + '.xlsx', index=False)
    report_df.to_json('reports/evaluation_report_' + args.dataset_name + '.json', force_ascii=False)
    with open('reports/evaluation_report_' + args.dataset_name + '.txt', 'w') as f:
        print(f'{nones} question unanswered!\n', file=f)
        print(f'{noisy_labels} noisy answers!\n', file=f)
        print(classification_report(y_true=labels, y_pred=predictions, target_names=label_names, zero_division=0,
                                    digits=3), file=f)


parser = argparse.ArgumentParser(description='Evaluate GPT')
parser.add_argument("--dataset_name", type=str, default='swiss_criticality_prediction_bge_considerations',
                    help="Name of dataset as stored on HF")
parser.add_argument("--model_name", type=str, default='gpt-3.5-turbo', help="GPT model name")
parser.add_argument("--multi_label", type=bool, default=False, help="Whether the task is multi-label")
parser.add_argument("--few_shot_k", type=int, default=None, help="Number of k-shots")

args = parser.parse_args()

main(args)
