import os
from pathlib import Path
import pandas as pd
import argparse

task_type_mapping = {
    "brazilian_court_decisions_judgment": "SLTC",
    "brazilian_court_decisions_unanimity": "SLTC",
    "german_argument_mining": "SLTC",
    "greek_legal_code_chapter": "SLTC",
    "greek_legal_code_subject": "SLTC",
    "greek_legal_code_volume": "SLTC",
    "swiss_judgment_prediction": "SLTC",
    "turkish_constitutional_court_decisions_judgment": "SLTC",
    "online_terms_of_service_unfairness_levels": "SLTC",
    "online_terms_of_service_clause_topics": "MLTC",
    "covid19_emergency_event": "MLTC",
    "multi_eurlex_level_1": "MLTC",
    "multi_eurlex_level_2": "MLTC",
    "multi_eurlex_level_3": "MLTC",
    "greek_legal_ner": "NER",
    "legalnero": "NER",
    "lener_br": "NER",
    "mapa_coarse": "NER",
    "mapa_fine": "NER",
    "original": "NER",
    "ecthr_a": "MLTC",
    "ecthr_b": "MLTC",
    "eurlex": "MLTC",
    "scotus": "SLTC",
    "ledgar": "SLTC",
    "unfair_tos": "MLTC",
    "case_hold": "MCQA",
    "swiss_criticality_prediction_bge_facts": "SLTC",
    "swiss_criticality_prediction_bge_considerations": "SLTC",
    "swiss_criticality_prediction_citation_facts": "SLTC",
    "swiss_criticality_prediction_citation_considerations": "SLTC",
    "swiss_law_area_prediction_facts": "SLTC",
    "swiss_law_area_prediction_considerations": "SLTC",
    "swiss_law_area_prediction_sub_area_facts": "SLTC",
    "swiss_law_area_prediction_sub_area_considerations": "SLTC",
    "swiss_judgment_prediction_xl_facts": "SLTC",
    "swiss_judgment_prediction_xl_considerations": "SLTC",
}

lextreme_configs = [
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
    "swiss_law_area_prediction_sub_area_facts"
]

zeroshot_output_path = 'zero-shot-predictions_lextreme_only'


def main(args):

    for config in swiss_legal_data_configs:
        command = f'python evaluate_perfomance.py --dataset_name {config} --model_name {args.model_name}'
        os.system(command)

    path = Path(f'reports/{args.model_name}/')

    all_results = list()
    for f in path.glob('**/*'):
        print(f)
        if f.is_file() and str(f).endswith('xlsx'):
            df = pd.read_excel(f)
            df = df.reset_index()
            all_results.append(df)
    all_results = pd.concat(all_results)
    # all_results['number_of_samples'] = all_results['support'] + all_results['question unanswered']
    all_results = all_results[
        ["finetuning_task", "metric", "micro avg", "macro avg", "weighted avg", "samples avg", "question unanswered",
         "noisy answers"]]
    all_results = all_results.drop_duplicates()
    all_results.to_excel(path / 'evaluation_report_final.xlsx')

parser = argparse.ArgumentParser(description='Evaluate Models.')
parser.add_argument("--model_name", type=str, help="Model name")

args = parser.parse_args()

main(args)
