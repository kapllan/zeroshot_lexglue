import os
import time

configs = [
    #"brazilian_court_decisions_judgment",
    #"brazilian_court_decisions_unanimity",
    #"german_argument_mining",
    # "greek_legal_code_chapter",
    # "greek_legal_code_subject",
    #"greek_legal_code_volume",
    #"swiss_judgment_prediction",
    #"online_terms_of_service_unfairness_levels",
    #"online_terms_of_service_clause_topics",
    "covid19_emergency_event"
    # "multi_eurlex_level_1",
    # "multi_eurlex_level_2",
    # "multi_eurlex_level_3",
    # "greek_legal_ner",
    # "legalnero",
    # "lener_br",
    # "mapa_coarse",
    # "mapa_fine"
]

for n in range(0, 10):
    for config in configs:
        zeroshot_output_path = 'zero-shot-predictions_lextreme_only'
        command = f'python call_openai.py --dataset_name {config} --model_name gpt-3.5-turbo --zeroshot_output_path {zeroshot_output_path}'
        os.system(command)
    time.sleep(5)
