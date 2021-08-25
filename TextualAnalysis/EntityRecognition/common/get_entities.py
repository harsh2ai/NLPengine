from transformers import pipeline
nlp = pipeline("ner")

def entity_details(text):
    ner_details = nlp(text)
    return ner_details


if __name__ == "__main__":
    nlp = pipeline("ner")
    entity_details("I live near Boston, what about you?", nlp)
