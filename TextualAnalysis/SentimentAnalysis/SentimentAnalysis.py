from TextualAnalysis.SentimentAnalysis.common.get_sentiment_analysis import get_sentiment_analysis


class GetSentiment():

    def sentiment_analysis(self, text):
        # Store language detection results
        sentiment_analysis = []

        # Iterating through data
        for line in text.split('\n')[:10]:
            columns = line.split('\t')
            columns = [col.strip() for col in columns]
            sentiment_analysis.append(get_sentiment_analysis(columns[1]))

        sentiment_analysis = [item for sublist in sentiment_analysis for item in sublist]
        return {'sentiment_analysis': sentiment_analysis}
