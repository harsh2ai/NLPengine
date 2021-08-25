""" Copyright 2021, Scanta Inc., All rights reserved. """

from TextualAnalysis.GetTextAnalysis.common.text_analysis import get_text_analysis
from nltk.corpus import stopwords
import nltk

class GetTextualAnalysis():

    def get_textual_analysis(self, txt_data):
        # Tokenizes a text to its words, removes and replaces some of them
        try:
            stoplist = stopwords.words('english')
        except:
            nltk.download('stopwords')
            stoplist = stopwords.words('english')

        # # extra stopwords
        my_stopwords = "multiexclamation multiquestion multistop url atuser st rd nd th am pm"
        # update stoplist
        stoplist = stoplist + my_stopwords.split()
        allowedWordTypes = ["J", "R", "V", "N"]
        #  J is Adjective, R is Adverb, V is Verb, N is Noun. These are used for POS Tagging
        # Run analysis for txt_data
        return {'count_analysis': get_text_analysis(txt_data, stoplist, allowedWordTypes, pos_tagging=True)}
