TEMPLATES = {'ecthr_a':
             {
                 'INPUT_INTRODUCTORY_TEXT': 'Given the following facts from a European Court of Human Rights (ECtHR) case:',
                 'OPTIONS_PRESENTATION_TEXT': 'Which article(s) of ECHR have been violated, if any, out of the following options:\n',
                 'QUESTION_TEXT': 'The relevant options are:'},
             'ecthr_b':
             {
                 'INPUT_INTRODUCTORY_TEXT': 'Given the following facts from a European Court of Human Rights (ECtHR) case:',
                 'OPTIONS_PRESENTATION_TEXT': 'Which article(s) of ECHR are relevant, if any, out of the following options:\n',
                 'QUESTION_TEXT': 'The relevant options are:'},
             'ecthr_b_v2':
             {
                 'INPUT_INTRODUCTORY_TEXT': 'Given the following facts from a European Court of Human Rights (ECtHR) opinion:',
                 'OPTIONS_PRESENTATION_TEXT': 'Which article(s) of the European Convention of Human Rights (ECHR) were considered in court, if any, out of the following options:\n',
                 'QUESTION_TEXT': 'The articles considered are:'},
             'scotus':
             {'INPUT_INTRODUCTORY_TEXT': 'Given the following opinion from the Supreme Court of USA (SCOTUS):',
                 'OPTIONS_PRESENTATION_TEXT': 'Which topics are relevant out of the following options:\n',
                 'QUESTION_TEXT': 'The relevant option is:'},
             'eurlex':
             {'INPUT_INTRODUCTORY_TEXT': 'Given the following excerpt from an EU law:',
                 'OPTIONS_PRESENTATION_TEXT': 'The EU law is relevant to some topics out of the following options:\n',
                 'QUESTION_TEXT': 'The relevant options are:'},
             'ledgar':
             {'INPUT_INTRODUCTORY_TEXT': 'Given the following contractual section:',
                 'OPTIONS_PRESENTATION_TEXT': 'There is an appropriate section title out of the following options:\n',
                 'QUESTION_TEXT': 'The most appropriate option is:'},
             'unfair_tos':
             {'INPUT_INTRODUCTORY_TEXT': 'Given the following sentence from an online Term of Services:',
                 'OPTIONS_PRESENTATION_TEXT': 'The sentence is unfair with respect to some of the following options:\n',
                 'QUESTION_TEXT': 'The relevant options are:'},
             'case_hold':
             {'INPUT_INTRODUCTORY_TEXT': 'Given the following excerpt from a US court opinion:',
                 'OPTIONS_PRESENTATION_TEXT': 'The [Masked Holding] is a placeholder for one of the following options:\n',
                 'QUESTION_TEXT': 'The relevant option is:'},
             'swiss_criticality_prediction_bge_considerations':
             {'INPUT_INTRODUCTORY_TEXT': 'Given the considerations from the following Swiss Federal Supreme Court Decision:',
                 'OPTIONS_PRESENTATION_TEXT': 'Federal Supreme Court Decisions in Switzerland that are published additionally get the label critical, those Federal Supreme Court Decisions that are not published additionally, get the label non-critical. Therefore, there are two labels to choose from: \n',
                 'QUESTION_TEXT': 'The relevant label in this case is:'},
             'swiss_criticality_prediction_bge_facts':
             {'INPUT_INTRODUCTORY_TEXT': 'Given the facts from the following Swiss Federal Supreme Court Decision:',
                 'OPTIONS_PRESENTATION_TEXT': 'Federal Supreme Court Decisions in Switzerland that are published additionally get the label critical, those Federal Supreme Court Decisions that are not published additionally, get the label non-critical. Therefore, there are two labels to choose from: \n',
                 'QUESTION_TEXT': 'The relevant label in this case is:'},
             'swiss_criticality_prediction_citation_considerations':
             {'INPUT_INTRODUCTORY_TEXT': 'Given the considerations from the following Swiss Federal Supreme Court Decision:',
                 'OPTIONS_PRESENTATION_TEXT': 'How likely is it that this Swiss Federal Supreme Court Decision gets cited. Choose between one of the following labels (a bigger number in the label means that the court decision is more likely to be cited): \n',
                 'QUESTION_TEXT': 'The relevant label in this case is:'},
             'swiss_criticality_prediction_citation_facts':
             {'INPUT_INTRODUCTORY_TEXT': 'Given the facts from the following Swiss Federal Supreme Court Decision:',
                 'OPTIONS_PRESENTATION_TEXT': 'How likely is it that this Swiss Federal Supreme Court Decision gets cited. Choose between one of the following labels (a bigger number in the label means that the court decision is more likely to be cited):  \n',
                 'QUESTION_TEXT': 'The relevant label in this case is:'},
             'swiss_judgment_prediction_xl_considerations':
             {'INPUT_INTRODUCTORY_TEXT': 'Given the considerations from the following court decision:',
                 'OPTIONS_PRESENTATION_TEXT': 'Will this court decision get approved or dismissed? There are two labels to choose from: \n',
                 'QUESTION_TEXT': 'The relevant label in this case is:'},
             'swiss_judgment_prediction_xl_facts':
             {'INPUT_INTRODUCTORY_TEXT': 'Given the facts from the following court decision:',
                 'OPTIONS_PRESENTATION_TEXT': 'Will this court decision get approved or dismissed? There are two labels to choose from: \n',
                 'QUESTION_TEXT': 'The relevant label in this case is:'},
             'swiss_law_area_prediction_facts':
             {'INPUT_INTRODUCTORY_TEXT': 'Given the facts from the following court decision:',
                 'OPTIONS_PRESENTATION_TEXT': 'Which topic/law area is relevant out of the following options:\n',
                 'QUESTION_TEXT': 'The relevant option is:'},
             'swiss_law_area_prediction_considerations':
             {'INPUT_INTRODUCTORY_TEXT': 'Given the considerations from the following court decision:',
                 'OPTIONS_PRESENTATION_TEXT': 'Which topic/law area is relevant out of the following options:\n',
                 'QUESTION_TEXT': 'The relevant option is:'},
             'swiss_law_area_prediction_sub_area_considerations':
             {'INPUT_INTRODUCTORY_TEXT': 'Given the considerations from the following court decision:',
                 'OPTIONS_PRESENTATION_TEXT': 'Which topic/law area is relevant out of the following options:\n',
                 'QUESTION_TEXT': 'The relevant option is:'},
             'swiss_law_area_prediction_sub_area_facts':
             {'INPUT_INTRODUCTORY_TEXT': 'Given the facts from the following court decision:',
                 'OPTIONS_PRESENTATION_TEXT': 'Which topic/law area is relevant out of the following options:\n',
                 'QUESTION_TEXT': 'The relevant option is:'},
             'brazilian_court_decisions_judgment':
             {'INPUT_INTRODUCTORY_TEXT': 'Given the following case description from a decision heard at the State Supreme Court of Alagoas (Brazil):',
                 'OPTIONS_PRESENTATION_TEXT': 'Predict whether the appeal will be denied or whether it is partially or fully favourable by using the following options: no = The appeal was denied, partial = For partially favourable decisions, yes = For fully favourable decisions. So, relevant options to choose from are:\n',
                 'QUESTION_TEXT': 'The relevant option in this case description is:'},
             'brazilian_court_decisions_unanimity':
             {'INPUT_INTRODUCTORY_TEXT': 'Given the following case description from a decision heard at the State Supreme Court of Alagoas (Brazil):',
                 'OPTIONS_PRESENTATION_TEXT': 'Predict how unanimously the judges will decide on whether the appeal will be denied or approved. So, relevant options to choose from are:\n',
                 'QUESTION_TEXT': 'The relevant option in this case description is:'},
             'german_argument_mining':
             {'INPUT_INTRODUCTORY_TEXT': 'Given the following sentence from a German court decisions:',
                 'OPTIONS_PRESENTATION_TEXT': 'The major components/labels of German Urteilsstil are: conclusion = Overall result, definition = Abstract legal facts and consequences, subsumption = Determination sentence / Concrete facts, other = Anything else. So, relevant options or labels to choose from are:\n',
                 'QUESTION_TEXT': 'The relevant option in this sentence is:'},
             'greek_legal_code_chapter': {'INPUT_INTRODUCTORY_TEXT': 'Given the following Greek legislative document:',
                                          'OPTIONS_PRESENTATION_TEXT': "Predict the chapter level category of the Permanent Greek Legislation Code - Raptarchis (Ραπτάρχης)' the document belongs to. So, the relevant categories to choose from are: \n",
                                          'QUESTION_TEXT': 'The relevant category in this Greek legislative document is:'},
             'greek_legal_code_subject': {'INPUT_INTRODUCTORY_TEXT': 'Given the following Greek legislative document:',
                                          'OPTIONS_PRESENTATION_TEXT': "Predict the subject level category of the Permanent Greek Legislation Code - Raptarchis (Ραπτάρχης)' the document belongs to. So, the relevant categories to choose from are: \n",
                                          'QUESTION_TEXT': 'The relevant category in this Greek legislative document is:'},
             'greek_legal_code_volume': {'INPUT_INTRODUCTORY_TEXT': 'Given the following Greek legislative document:',
                                         'OPTIONS_PRESENTATION_TEXT': "Predict the volume level category of the Permanent Greek Legislation Code - Raptarchis (Ραπτάρχης)' the document belongs to. So, the relevant categories to choose from are: \n",
                                         'QUESTION_TEXT': 'The relevant category in this Greek legislative document is:'},
             'swiss_judgment_prediction': {'INPUT_INTRODUCTORY_TEXT': 'Given the following facts description from a decision heard at the Swiss Federal Supreme Court: ',
                                           'OPTIONS_PRESENTATION_TEXT': "Predict the judgment of the case (approval: The appeal was approved, or dismissal: The appeal was denied). So, the relevant options to choose from are: \n",
                                           'QUESTION_TEXT': 'The relevant option in this facts description is:'},
             'online_terms_of_service_unfairness_levels': {'INPUT_INTRODUCTORY_TEXT': 'Given the following sentence from a Terms of Service(ToS) document: ',
                                                           'OPTIONS_PRESENTATION_TEXT': "Predict the unfairness level of the sentence (potentially_unfair, clearly_unfair, clearly_fair, untagged). So, the relevant options to choose from are: \n",
                                                           'QUESTION_TEXT': 'The relevant option in this facts description is:'},
             'covid19_emergency_event': {'INPUT_INTRODUCTORY_TEXT': 'Given the following sentence from a European legislative document: ',
                                         'OPTIONS_PRESENTATION_TEXT':
                                         '''Predict the applicable measurements against COVID-19 out of the following: "
                                         event1: State of Emergency, 
                                         event2: Restrictions of fundamental rights and civil liberties, 
                                         event3: Restrictions of daily liberties, 
                                         event4: Closures / lockdown, 
                                         event5: Suspension of international cooperation and commitments, 
                                         event6: Police mobilization, 
                                         event7: Army mobilization, 
                                         event8: Government oversight.'''+"If there is no label reply n/a, if there are multiple labels specify all of them separated by a comma. So, the relevant labels to choose from are: \n",
                                         'QUESTION_TEXT': 'The relevant labels in this sentence are:'},
             'online_terms_of_service_clause_topics': {'INPUT_INTRODUCTORY_TEXT': 'Given the following sentence from a Terms of Service(ToS) document: ',
                                                       'OPTIONS_PRESENTATION_TEXT': '''Predict the clause topics of the sentence out of the following:
                                                       a: Arbitration, 
                                                       b: Unilateral change,
                                                       c: Content removal,
                                                       d: Jurisdiction, 
                                                       e: Choice of law, 
                                                       f: Limitation of liability, 
                                                       g: Unilateral termination, 
                                                       h: Contract by using, 
                                                       i: Privacy included.
                                                       ''' + "If there is no label reply n/a, if there are multiple labels specify all of them separated by a comma. So, the relevant labels to choose from are: \n",
                                                       'QUESTION_TEXT': 'The relevant labels in this sentence are:'},
             'multi_eurlex_level_1': {'INPUT_INTRODUCTORY_TEXT': 'Given the following a document from an EU law: ',
                                      'OPTIONS_PRESENTATION_TEXT': "Predict the level 1 concept in the EUROVOC taxonomy. If there is no label reply n/a, if there are multiple labels specify all of them separated by a comma. The relevant labels to choose from are: \n",
                                      'QUESTION_TEXT': 'The relevant labels in this document are:'},
             'multi_eurlex_level_2': {'INPUT_INTRODUCTORY_TEXT': 'Given the following a document from an EU law: ',
                                      'OPTIONS_PRESENTATION_TEXT': "Predict the level 2 concept in the EUROVOC taxonomy. If there is no label reply n/a, if there are multiple labels specify all of them separated by a comma. The relevant labels to choose from are: \n",
                                      'QUESTION_TEXT': 'The relevant labels in this document are:'},
             'multi_eurlex_level_3': {'INPUT_INTRODUCTORY_TEXT': 'Given the following a document from an EU law: ',
                                      'OPTIONS_PRESENTATION_TEXT': "Predict the level 3 concept in the EUROVOC taxonomy. If there is no label reply n/a, if there are multiple labels specify all of them separated by a comma. The relevant labels to choose from are: \n",
                                      'QUESTION_TEXT': 'The relevant labels in this document are:'},
             'greek_legal_ner': {'INPUT_INTRODUCTORY_TEXT': 'Given the following a sentence from Greek legislation: ',
                                 'OPTIONS_PRESENTATION_TEXT': "Using the IOB2 format. Predict the named entity type for each token out of the following: \n",
                                 'QUESTION_TEXT': 'The relevant named entity types in this sentence are:'},
             'legalnero': {'INPUT_INTRODUCTORY_TEXT': 'Given the following a sentence from Romanian legislation: ',
                           'OPTIONS_PRESENTATION_TEXT': "Using the IOB2 format. Predict the named entity type for each token out of the following: \n",
                           'QUESTION_TEXT': 'The relevant named entity types in this sentence are:'},
             'lener_br': {'INPUT_INTRODUCTORY_TEXT': 'Given the following a sentence from Brazilian legal documents (court decisions and legislation): ',
                          'OPTIONS_PRESENTATION_TEXT': "Using the IOB2 format. Predict the named entity type for each token out of the following: \n",
                          'QUESTION_TEXT': 'The relevant named entity types in this sentence are:'},
             'mapa_coarse': {'INPUT_INTRODUCTORY_TEXT': 'Given the following a sentence from the EUR-Lex database: ',
                             'OPTIONS_PRESENTATION_TEXT': "Using the IOB2 format. Predict the coarse-grained named entity type for each token out of the following: \n",
                             'QUESTION_TEXT': 'The relevant named entity types in this sentence are:'},
             'mapa_fine': {'INPUT_INTRODUCTORY_TEXT': 'Given the following a sentence from the EUR-Lex database: ',
                           'OPTIONS_PRESENTATION_TEXT': "Using the IOB2 format. Predict the fine-grained named entity type for each token out of the following: \n",
                           'QUESTION_TEXT': 'The relevant named entity types in this sentence are:'},



             }
