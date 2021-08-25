import spacy
from MLCommon.utils import get_dict_from_txt
from spacy.language import Language
from spacy_langdetect import LanguageDetector


def create_lang_detector(nlp, name):
    return LanguageDetector()


Language.factory("language_detector", func=create_lang_detector)

nlp = spacy.load('en_core_web_sm')
nlp.max_length = 2000000
nlp.add_pipe('language_detector', last=True)


def detect_lang(text):
    doc = nlp(text)
    detect_language = doc._.language
    return detect_language


def map_lang_name(language):
    language_map = get_dict_from_txt('MLData/TextAnalysisData/lang_codes.txt')
    lang_full_form = language_map[language['language']]
    lang_details = {'language_code': language['language'],
                    'language': lang_full_form,
                    'score': round(language['score'], 3)}
    return lang_details


if __name__ == "__main__":
    text_content = "Er lebt mit seinen Eltern und seiner Schwester in Berlin."
    language = detect_lang(text_content)
    print("Score from spacy:", language)
    lang_details = map_lang_name(language)
    print("Language detected:", lang_details)
