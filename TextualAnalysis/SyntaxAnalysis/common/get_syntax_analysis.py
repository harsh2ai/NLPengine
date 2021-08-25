import collections
import itertools
import os

import stanza

# stanza.download('en')

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
'''Global Parameter'''
nlp = stanza.Pipeline('en')


class NLPStanzaAnalysis():

    def word_level_analysis(self, sentence):
        word_report = []
        report = nlp(sentence)
        for sent in report.sentences:
            for items in sent.tokens:
                word_report.append(items.to_dict())
        word_report = list(itertools.chain(*word_report))
        return word_report

    def percent_calculate(self, attribs):
        params = {}
        for items in attribs[:1]:
            counter = collections.Counter()
            for line in items:
                counter[line.lower()] += 1
            del counter['']
            total = sum(counter.values())
            for word, count in sorted(counter.items(), key=lambda t: t[1], reverse=True):
                params[word] = round(count / total * 100, 2)
        return params

    def percentage_analysis(self, sentence):
        word_report = self.word_level_analysis(sentence)
        pos = []
        ner_tag = []
        deprel = []
        for i in word_report:
            pos.append(i['upos'])
            ner_tag.append(i['ner'])
            deprel.append(i['deprel'])  # dependency parsing details
        attribs = [pos, ner_tag, deprel]
        return self.percent_calculate(attribs)


if __name__ == "__main__":
    text = "i want to change my password.Can you help"
    print(text)
    nlp_s = NLPStanzaAnalysis()
    print(nlp_s.percentage_analysis(text))
