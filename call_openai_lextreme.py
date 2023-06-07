import os

configs = [
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

for config in configs:
    command = 'python call_openai.py --dataset_name ' + config + ' --model_name gpt-3.5-turbo'
    os.system(command)
