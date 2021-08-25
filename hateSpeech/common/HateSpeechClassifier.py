
import pickle
import numpy as np
import pandas as pd
#from sklearn.externals.joblib import joblib
from sklearn.svm import LinearSVC
from sklearn.linear_model import LogisticRegression
from sklearn.feature_selection import SelectFromModel
from sklearn.feature_extraction.text import TfidfVectorizer
import nltk
from nltk.stem.porter import *
import string
import re
import joblib


from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer as VS
from textstat.textstat import *



class HateSpeechClassifier():
    '''
    '''
    def __init__(self):
        '''
        Load the saved models and other resources
        '''
        self.stopwords=stopwords = nltk.corpus.stopwords.words("english")
        other_exclusions = ["#ff", "ff", "rt"]
        self.stopwords.extend(other_exclusions)
        self.sentiment_analyzer = VS()
        self.stemmer = PorterStemmer()
        print("Loading trained classifier... ")
        self.model = joblib.load('./hateSpeech/modals/final_model.pkl')

        print("Loading other information...")
        self.tf_vectorizer = joblib.load('./hateSpeech/modals/final_tfidf.pkl')
        self.idf_vector = joblib.load('./hateSpeech/modals/final_idf.pkl')
        self.pos_vectorizer = joblib.load('./hateSpeech/modals/final_pos.pkl')
        #Load ngram dict
        #Load pos dictionary
        #Load function to transform data


    def preprocess(self,text_string):
        """
        Accepts a text string and replaces:
        1) urls with URLHERE
        2) lots of whitespace with one instance
        3) mentions with MENTIONHERE

        This allows us to get standardized counts of urls and mentions
        Without caring about specific people mentioned
        """
        space_pattern = '\s+'
        giant_url_regex = ('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|'
            '[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')
        mention_regex = '@[\w\-]+'
        parsed_text = re.sub(space_pattern, ' ', text_string)
        parsed_text = re.sub(giant_url_regex, 'URLHERE', parsed_text)
        parsed_text = re.sub(mention_regex, 'MENTIONHERE', parsed_text)
        #parsed_text = parsed_text.code("utf-8", errors='ignore')
        return parsed_text

    def tokenize(self,text):
        """Removes punctuation & excess whitespace, sets to lowercase,
        and stems tweets. Returns a list of stemmed tokens."""
        text = " ".join(re.split("[^a-zA-Z]*", text.lower())).strip()
        #tokens = re.split("[^a-zA-Z]*", text.lower())
        tokens = [self.stemmer.stem(t) for t in text.split()]
        return tokens

    def basic_tokenize(self,text):
        """Same as tokenize but without the stemming"""
        text = " ".join(re.split("[^a-zA-Z.,!?]*", text.lower())).strip()
        return text.split()

    def get_pos_tags(self,text):
        """Takes a list of strings (tweets) and
        returns a list of strings of (POS tags).
        """
        text_tags = []
        for t in text:
            tokens = basic_tokenize(preprocess(t))
            tags = nltk.pos_tag(tokens)
            tag_list = [x[1] for x in tags]
            #for i in range(0, len(tokens)):
            tag_str = " ".join(tag_list)
            text_tags.append(tag_str)
        return text_tags

    def count_twitter_objs(self,text_string):
        """
        Accepts a text string and replaces:
        1) urls with URLHERE
        2) lots of whitespace with one instance
        3) mentions with MENTIONHERE
        4) hashtags with HASHTAGHERE

        This allows us to get standardized counts of urls and mentions
        Without caring about specific people mentioned.

        Returns counts of urls, mentions, and hashtags.
        """
        space_pattern = '\s+'
        giant_url_regex = ('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|'
            '[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')
        mention_regex = '@[\w\-]+'
        hashtag_regex = '#[\w\-]+'
        parsed_text = re.sub(space_pattern, ' ', text_string)
        parsed_text = re.sub(giant_url_regex, 'URLHERE', parsed_text)
        parsed_text = re.sub(mention_regex, 'MENTIONHERE', parsed_text)
        parsed_text = re.sub(hashtag_regex, 'HASHTAGHERE', parsed_text)
        return(parsed_text.count('URLHERE'),parsed_text.count('MENTIONHERE'),parsed_text.count('HASHTAGHERE'))

    def other_features_(self,text):
        """This function takes a string and returns a list of features.
        These include Sentiment scores, Text and Readability scores,
        as well as Twitter specific features.

        This is modified to only include those features in the final
        model."""

        sentiment = self.sentiment_analyzer.polarity_scores(text)

        words = preprocess(text) #Get text only

        syllables = textstat.syllable_count(words) #count syllables in words
        num_chars = sum(len(w) for w in words) #num chars in words
        num_chars_total = len(tweet)
        num_terms = len(text.split())
        num_words = len(words.split())
        avg_syl = round(float((syllables+0.001))/float(num_words+0.001),4)
        num_unique_terms = len(set(words.split()))

        ###Modified FK grade, where avg words per sentence is just num words/1
        FKRA = round(float(0.39 * float(num_words)/1.0) + float(11.8 * avg_syl) - 15.59,1)
        ##Modified FRE score, where sentence fixed to 1
        FRE = round(206.835 - 1.015*(float(num_words)/1.0) - (84.6*float(avg_syl)),2)

        twitter_objs = count_twitter_objs(text) #Count #, @, and http://
        features = [FKRA, FRE, syllables, num_chars, num_chars_total, num_terms, num_words,
                    num_unique_terms, sentiment['compound'],
                    twitter_objs[2], twitter_objs[1],]
        #features = pandas.DataFrame(features)
        return features

    def get_oth_features(self,text):
        """Takes a list of tweets, generates features for
        each tweet, and returns a numpy array of tweet x features"""
        feats=[]
        for t in text:
            feats.append(other_features_(t))
        return np.array(feats)


    def transform_inputs(self,text):
        """
        This function takes a list of tweets, along with used to
        transform the tweets into the format accepted by the model.

        Each tweet is decomposed into
        (a) An array of TF-IDF scores for a set of n-grams in the tweet.
        (b) An array of POS tag sequences in the tweet.
        (c) An array of features including sentiment, vocab, and readability.

        Returns a pandas dataframe where each row is the set of features
        for a tweet. The features are a subset selected using a Logistic
        Regression with L1-regularization on the training data.

        """
        tf_array = self.tf_vectorizer.fit_transform(text).toarray()
        tfidf_array = tf_array*self.idf_vector
        print("Built TF-IDF array")

        pos_tags = get_pos_tags(tweets)
        pos_array = self.pos_vectorizer.fit_transform(pos_tags).toarray()
        print("Built POS array")

        oth_array = self.get_oth_features(tweets)
        print("Built other feature array")

        M = np.concatenate([tfidf_array, pos_array, oth_array],axis=1)
        return pd.DataFrame(M)

    def predictions(self,X, model):
        """
        This function calls the predict function on
        the trained model to generated a predicted y
        value for each observation.
        """
        y_preds = self.model.predict(X)
        return y_preds

    def class_to_name(self,class_label):
        """
        This function can be used to map a numeric
        feature name to a particular class.
        """
        if class_label == 0:
            return "Hate speech"
        elif class_label == 1:
            return "Offensive language"
        elif class_label == 2:
            return "Neither"
        else:
            return "No label"

    def get_prediction(text, perform_prints=True):

        print("Transforming inputs...")
        X = transform_inputs(text)

        print("Running classification model...")
        predicted_class = predictions(X, self.model)
        return predicted_class




if __name__=="__main__":
    p=HateSpeechClassifier().get_prediction("Bull Shit!!")
    print(p)