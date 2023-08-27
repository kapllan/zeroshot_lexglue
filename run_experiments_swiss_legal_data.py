import os
import time

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

print('Starting with claude-2.')
for n in range(0, 1):
    for config in configs:
        command = f'python call_other_models.py --dataset_name {config} --model_name claude-2'
        os.system(command)
    time.sleep(5)


print('Starting with llama.')
for n in range(0, 1):
    for config in configs:
        command = f'python call_other_models.py --dataset_name {config} --model_name llama-2-70b-chat-hf'
        os.system(command)
    time.sleep(5)


'''for n in range(0, 10):
    for config in configs:
        command = 'python call_openai.py --dataset_name ' + config + ' --model_name gpt-3.5-turbo'
        os.system(command)
    time.sleep(5)'''
