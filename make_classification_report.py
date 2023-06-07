import os
from pathlib import Path
import pandas as pd

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

for config in swiss_legal_data_configs:
    command = 'python evaluate_perfomance.py --dataset_name ' + config
    os.system(command)

path = Path('reports/')

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
all_results.to_excel(path / 'evaluation_report.xlsx')
