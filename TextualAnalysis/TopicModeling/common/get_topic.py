import re
import nltk
import gensim
from nltk.stem.porter import *
from gensim.corpora import Dictionary
from gensim.utils import simple_preprocess
from gensim.parsing.preprocessing import STOPWORDS
from nltk.stem import WordNetLemmatizer, SnowballStemmer
from strsimpy.levenshtein import Levenshtein
from collections import Counter

'''Global Parameters'''
levenshtein = Levenshtein()


class TopicModel():
    """---------Func: To preprocess and stem the language data-----------"""

    def preprocess(text):
        stemmer = SnowballStemmer("english")
        result = []
        for token in gensim.utils.simple_preprocess(text):
            if token not in gensim.parsing.preprocessing.STOPWORDS and len(token) > 3:
                result.append(stemmer.stem(WordNetLemmatizer().lemmatize(token, pos='v')))
        return result

    '''---------Func: To convert string into vectors-----------'''
    '''- Count the characters in word
       - Precomputes a set of the different characters
       - Precomputes the "length" of the word vector
       Returns : tuple '''

    def word2vec(word):
        cw = Counter(word)
        sw = set(cw)
        lw = sqrt(sum(c * c for c in cw.values()))
        return cw, sw, lw

    '''---------Func: Bow for gpt2 text-----------'''

    def gen_topic(text_processed, text_dict):
        bow_corpus = [text_dict.doc2bow(doc) for doc in [text_processed]]
        topics = []
        for i in range(len(bow_corpus[0])):
            topics.append(text_dict[bow_corpus[0][i][0]])
        return topics

    '''---------Func: Levenshtien distance between topics-----------'''

    def lev_dis(topics):
        top_dict = {}
        topics = [(topics[i], topics[j]) for i in range(len(topics)) for j in range(i + 1, len(topics))]
        for i in topics:
            hw = i[0]
            gw = i[1]
            top_dict.update({hw + "-" + gw: levenshtein.distance(hw, gw)})
        return top_dict

    '''---------Performing Linear Discriminant Analysis on BOW Dictionary--------'''

    def lda_model(bow_corpus, text_dict):
        lda_model = gensim.models.LdaMulticore(bow_corpus,
                                               num_topics=5,
                                               id2word=text_dict,
                                               passes=10,
                                               workers=2)
        for i in lda_model.print_topics(-1):
            topics = list(re.findall('"([^"]*)"', i[1]))
            print(topics)

    def topic_modelling(text):
        text_processed = TopicModel.preprocess(text)
        text_dict = Dictionary([text_processed])
        topics = TopicModel.gen_topic(text_processed, text_dict)
        lev_dis = TopicModel.lev_dis(topics)
        # max_dis = max(lev_dis.items(), key=lambda x: x[1])
        return topics, lev_dis


if __name__ == "__main__":
    text = "i want to change my password.Can you help?"
    print(text)
    print(TopicModel.topic_modelling(text))
