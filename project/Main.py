import spacy
import warnings
import os
import coreferee
import benepar
import stanza
import spacy_stanza
from spacy import displacy
from spacy_wordnet.wordnet_annotator import WordnetAnnotator

from AnalyzeSentence import analyze_document
from AnalyzeText import determine_marker, correct_order, construct
from Structure.Block import ConditionBlock
from Utilities import find_dependency, text_pre_processing


def download_all_dependencies():
    import nltk
    import ssl
    try:
        _create_unverified_https_context = ssl._create_unverified_context
    except AttributeError:
        pass
    else:
        ssl._create_default_https_context = _create_unverified_https_context

    # benepar.download('benepar_en3')
    # benepar.download('benepar_en3_large')
    # nltk.download('wordnet')


if __name__ == '__main__':
    os.environ['TRANSFORMERS_NO_ADVISORY_WARNINGS'] = 'true'
    warnings.filterwarnings('ignore')
    # download_all_dependencies()

    # nlp = spacy.load('en_core_web_sm')
    nlp = spacy.load('en_core_web_trf')
    # nlp = spacy_stanza.load_pipeline("en", download_method=None)

    nlp.add_pipe('benepar', config={'model': 'benepar_en3'})
    # nlp.add_pipe('benepar', config={'model': 'benepar_en3_large'})

    nlp.add_pipe("spacy_wordnet", after='tagger')
    # nlp.add_pipe("spacy_wordnet")

    nlp.add_pipe('coreferee')

    text_input = open('Text/text08.txt', 'r').read().replace('\n', ' ')
    # text_input = "If an error is detected another arbitrary repair activity is executed. Otherwise, the repair is finished."



    text_input = text_pre_processing(text_input)
    document = nlp(text_input)
    document._.coref_chains.print()
    print()

    containerList = analyze_document(document)
    for container in containerList:
        determine_marker(container, nlp)
    correct_order(containerList)

    linked_list = construct(containerList)
    print(linked_list)




    # for file in os.listdir("Text"):
    #     if file == "__pycache__":
    #         continue
    #     print("*" * 50)
    #     print(file)
    #     text_input = open('Text/' + file, 'r').read().replace('\n', ' ')
    #
    #     text_input = text_pre_processing(text_input)
    #     document = nlp(text_input)
    #     document._.coref_chains.print()
    #     print()
    #
    #
    #     containerList = analyze_document(document)
    #     for container in containerList:
    #         determine_marker(container, nlp)
    #     correct_order(containerList)
    #
    #     linked_list = construct(containerList)
    #     print(linked_list)
    #     print("*" * 50)

