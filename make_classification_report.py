import os
from pathlib import Path
import pandas as pd

task_type_mapping= {
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
    "case_hold": "MCQA"
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

zeroshot_output_path = 'zero-shot-predictions_lextreme_only'

for config in lextreme_configs:
    if task_type_mapping[config]=='MLTC':
        command = f'python evaluate_perfomance.py --multi_label TRUE --dataset_name {config} --zeroshot_output_path {zeroshot_output_path}'
    
    else:
        command = f'python evaluate_perfomance.py --dataset_name {config} --zeroshot_output_path {zeroshot_output_path}'
    os.system(command)

path = Path(f'reports/{zeroshot_output_path}/')

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
all_results.to_excel(path / 'evaluation_report_lextreme.xlsx')
