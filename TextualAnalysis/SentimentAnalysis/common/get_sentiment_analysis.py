from transformers import pipeline

classifier = pipeline('sentiment-analysis')


def get_sentiment_analysis(text):
    sentiments = []
    results = classifier([text])
    for result in results:
        sentiments.append({'text': text, 'label': {result['label']}, 'score': round(result['score'], 4)})
    return sentiments
