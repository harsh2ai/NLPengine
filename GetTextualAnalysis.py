""" Copyright 2021, Scanta Inc., All rights reserved. """

import os

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

from MLCommon.utils import read_txt_files
from TextualAnalysis.EntityRecognition.EntityRecognition import GetEntity
from TextualAnalysis.GetTextAnalysis.GetTextAnalysis import GetTextualAnalysis
from TextualAnalysis.LanguageDetection.LanguageDetection import GetLanguage
from TextualAnalysis.SentimentAnalysis.SentimentAnalysis import GetSentiment
from TextualAnalysis.SyntaxAnalysis.SyntaxAnalysis import GetSyntax
from TextualAnalysis.TopicModeling.TopicModeling import GetTopic

class TextualAnalysis():

    def check_entity_recognition(self, text):
        model = GetEntity()
        entity_details = model.get_ner(text)
        return entity_details

    def check_language_detection(self, text):
        model = GetLanguage()
        langauge_deatils = model.language_detection(text)
        return langauge_deatils

    def check_sentiment_analysis(self, text):
        model = GetSentiment()
        sentiment_details = model.sentiment_analysis(text)
        return sentiment_details

    def check_syntax_analysis(self, text):
        model = GetSyntax()
        syntax_details = model.syntax_analysis(text)
        return syntax_details

    def check_topic_modeling(self, text):
        model = GetTopic()
        topic_details = model.topicmodeling(text)
        return topic_details

    def get_textual_analysis(self, text):
        model = GetTextualAnalysis()
        textual_analysis_details = model.get_textual_analysis(text)
        return textual_analysis_details


if __name__ == "__main__":
    print("Main Textual Analysis Model")

    # Pass data: Path to train data
    training_file_path = 'MLData/TextAnalysisData/ss-twitterfinal.txt'

    # Reading content of the txt file
    txt_data = read_txt_files(training_file_path)

    # Run analysis for txt_data
    se_model = TextualAnalysis()

    # Run analysis for txt_data
    count_analysis = se_model.get_textual_analysis(txt_data)
    print(count_analysis)
    print("***********")

    # Entity model
    ner_detection = se_model.check_entity_recognition(txt_data)
    print(ner_detection)
    print("***********")

    # Language model
    language_detection = se_model.check_language_detection(txt_data)
    print(language_detection)
    print("***********")

    # Sentiment model
    sentiment_detection = se_model.check_sentiment_analysis(txt_data)
    print(sentiment_detection)
    print("***********")

    # Syntax model
    syntax_analysis = se_model.check_syntax_analysis(txt_data)
    print(syntax_analysis)
    print("***********")

    # Topic Modeling
    topic_analysis = se_model.check_topic_modeling(txt_data)
    print(topic_analysis)
    print("***********")
