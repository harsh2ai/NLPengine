""" Copyright 2021, Scanta Inc., All rights reserved. """
import string
from time import time

from TextualAnalysis.GetTextAnalysis.common.analysis_count import *
from TextualAnalysis.GetTextAnalysis.common.negation_analysis import *
from TextualAnalysis.GetTextAnalysis.common.spellcheck import *
from TextualAnalysis.GetTextAnalysis.common.text_cleaning import *
from nltk import PorterStemmer
from nltk import WordNetLemmatizer

# set lemmatizer
lemmatizer = WordNetLemmatizer()

# set stemmer
stemmer = PorterStemmer()


def tokenize(text,finalTokens, stoplist, allowedWordTypes, pos_tagging=False):
    # Text features counts to be fetched
    totalAdjectives = 0
    totalAdverbs = 0
    totalVerbs = 0
    totalNouns = 0

    # tokens of one sentence each time
    onlyOneSentenceTokens = []

    # Find "not" and antonym for the next word and if found,
    # replaces not and the next word with the antonym
    # tokens = replaceNegations(tokens)

    translator = str.maketrans('', '', string.punctuation)

    # Remove punctuation
    text = text.translate(translator)

    # word_tokenize takes a text as an input and provides a list of every token in it
    try:
        tokens = nltk.word_tokenize(text)
    except:
        nltk.download('punkt')
        tokens = nltk.word_tokenize(text)

    if pos_tagging:
        # print("POS TAGGING BEGIN")
        # POS TAGGING BEGIN (If you want to exclude words using POS Tagging,
        # keep this section uncommented and comment the above)
        try:
            tagged = nltk.pos_tag(tokens)
        except:
             nltk.download('averaged_perceptron_tagger')
             tagged = nltk.pos_tag(tokens)
        # Part of speech tagging
        for w in tagged:
            if (w[1][0] in allowedWordTypes and w[0] not in stoplist):
                if w[1][0] == 'J':
                    totalAdjectives = +1
                elif w[1][0] == 'R':
                    totalAdverbs = +1
                elif w[1][0] == 'V':
                    totalVerbs = +1
                elif w[1][0] == 'N':
                    totalNouns = +1

                final_word = addCapTag(w[0])
                # final_word = final_word.lower()
                try:
                    final_word = replaceElongated(final_word)
                except:
                    nltk.download('wordnet')
                    final_word = replaceElongated(final_word)
                if len(final_word) > 1:
                    final_word = spellCorrection(final_word)
                final_word = lemmatizer.lemmatize(final_word)
                final_word = stemmer.stem(final_word)
                # POS TAGGING END
                onlyOneSentenceTokens.append(final_word)
                finalTokens.append(final_word)

    else:
        # print("Continue without POS TAGGING")
        # NO POS TAGGING BEGIN (If you don't want to use POS Tagging keep this section uncommented)

        # iterate through each tokens
        for w in tokens:

            # Remove stopwords
            if (w not in stoplist):

                # Finds a word with at least 3 characters capitalized and adds the tag ALL_CAPS_
                final_word = addCapTag(w)

                # Lowercases all characters
                final_word = final_word.lower()

                # Replaces an elongated word with its basic form, unless the word exists in the lexicon
                final_word = replaceElongated(final_word)

                if len(final_word) > 1:
                    # Correction of spelling errors
                    final_word = spellCorrection(final_word)

                # Technique Lemmatizes words
                final_word = lemmatizer.lemmatize(final_word)

                # Apply stemming to words
                final_word = stemmer.stem(final_word)

                # NO POS TAGGING END
                onlyOneSentenceTokens.append(final_word)
                finalTokens.append(final_word)

    onlyOneSentence = " ".join(onlyOneSentenceTokens)  # form again the sentence from the list of tokens
    # print(onlyOneSentence) # print final sentence

    """ Write the preprocessed text to file 
    with open("MLData/TextAnalysisData/result.txt", "a") as result:
        result.write(textID + "\t" + y + "\t" + onlyOneSentence + "\n")
    """
    return finalTokens, totalVerbs, totalAdverbs, totalAdjectives, totalNouns


def get_text_analysis(text, stoplist, allowedWordTypes, pos_tagging=True):
    t0 = time()
    finalTokens = []  # all tokens
    totalSentences = 0
    totalEmoticons = 0
    totalSlangs = 0
    totalSlangsFound = []
    totalElongated = 0
    totalMultiExclamationMarks = 0
    totalMultiQuestionMarks = 0
    totalMultiStopMarks = 0
    totalAllCaps = 0
    totalVerbs = 0
    totalAdverbs = 0
    totalAdjectives = 0
    totalNouns = 0
    tokens = []

    analysis_details = {}
    totalSentences += 1

    text = removeUnicode(text)  # Technique 0
    # print(text) # print initial text
    wordCountBefore = len(re.findall(r'\w+', text))  # word count of one sentence before preprocess

    # print("Words before preprocess: ", wordCountBefore, "\n")

    text = replaceURL(text)  # Technique 1
    text = replaceAtUser(text)  # Technique 1
    text = removeHashtagInFrontOfWord(text)  # Technique 1

    temp_slangs, temp_slangsFound = countSlang(text)
    totalSlangs += temp_slangs  # total slangs for all sentences
    for word in temp_slangsFound:
        totalSlangsFound.append(word)  # all the slangs found in all sentences

    text = replaceSlang(text)  # Technique 2: replaces slang words and abbreviations with their equivalents
    text = replaceContraction(text)  # Technique 3: replaces contractions to their equivalents
    text = removeNumbers(text)  # Technique 4: remove integers from text

    emoticons = countEmoticons(text)  # how many emoticons in this sentence
    totalEmoticons += emoticons

    text = removeEmoticons(text)  # removes emoticons from text

    totalAllCaps += countAllCaps(text)

    totalMultiExclamationMarks += countMultiExclamationMarks(
        text)  # how many repetitions of exclamation marks in this sentence
    totalMultiQuestionMarks += countMultiQuestionMarks(
        text)  # how many repetitions of question marks in this sentence
    totalMultiStopMarks += countMultiStopMarks(text)  # how many repetitions of stop marks in this sentence

    text = replaceMultiExclamationMark(
        text)  # Technique 5: replaces repetitions of exclamation marks with the tag "multiExclamation"
    text = replaceMultiQuestionMark(
        text)  # Technique 5: replaces repetitions of question marks with the tag "multiQuestion"
    text = replaceMultiStopMark(text)  # Technique 5: replaces repetitions of stop marks with the tag "multiStop"

    totalElongated += countElongated(text)  # how many elongated words emoticons in this sentence

    tokens, tV, tAdv, tAdj, tN = tokenize(text,finalTokens,
                                            stoplist, allowedWordTypes, pos_tagging)
    totalNouns = totalNouns + tN
    totalAdjectives = totalAdjectives + tAdj
    totalAdverbs = totalAdverbs + tAdv
    totalVerbs = totalVerbs + tV

    print("Total sentences: ", totalSentences)
    print("Total Words before preprocess: ", len(re.findall(r'\w+', text)))
    print("Total Distinct Tokens before preprocess: ", len(set(re.findall(r'\w+', text))))
    print("Average word/sentence before preprocess: ", len(re.findall(r'\w+', text)) / totalSentences)
    print("Total Words after preprocess: ", len(tokens))
    print("Total Distinct Tokens after preprocess: ", len(set(tokens)))
    print("Average word/sentence after preprocess: ", len(tokens) / totalSentences)

    print("Total verb count: ", totalVerbs)
    print("Total adverb count: ", totalAdverbs)
    print("Total adjective count: ", totalAdjectives)
    print("Total noun count: ", totalNouns)

    print("Total emoticons: ", totalEmoticons)
    print("Total slangs: ", totalSlangs)
    commonSlangs = nltk.FreqDist(totalSlangsFound)
    d1, d2 = {}, {}
    for (word, count) in commonSlangs.most_common(20):  # most common slangs across all texts
        d1[word] = count
    print("Most popular slangs:\n", d1)

    # print("Most popular slangs",commonSlangs) # plot most common slangs

    print("Total elongated words: ", totalElongated)
    print("Total multi exclamation marks: ", totalMultiExclamationMarks)
    print("Total multi question marks: ", totalMultiQuestionMarks)
    print("Total multi stop marks: ", totalMultiStopMarks)
    print("Total all capitalized words: ", totalAllCaps)

    # print(tokens)
    commonWords = nltk.FreqDist(tokens)
    print("Most common words:")
    for (word, count) in commonWords.most_common(10):  # most common words across all texts
        d2[word] = count
    print(d2)
    # commonWords.plot(100, cumulative=False)  # plot most common words

    bgm = nltk.collocations.BigramAssocMeasures()
    tgm = nltk.collocations.TrigramAssocMeasures()
    bgm_finder = nltk.collocations.BigramCollocationFinder.from_words(tokens)
    tgm_finder = nltk.collocations.TrigramCollocationFinder.from_words(tokens)
    bgm_finder.apply_freq_filter(5)  # bigrams that occur at least 5 times
    print("Most common collocations (bigrams)")
    print(bgm_finder.nbest(bgm.pmi, 5))  # top 50 bigram collocations
    bigms = tgm_finder.apply_freq_filter(5)  # trigrams that occur at least 5 times

    trigms = []
    if len(tgm_finder.nbest(tgm.pmi, 5)) > 1:
        print("Most common collocations (trigrams)")
        print(tgm_finder.nbest(tgm.pmi, 5))  # top 20 trigrams collocations
        trigms = tgm_finder.nbest(tgm.pmi, 5)

    print("Total run time: ", time() - t0, " seconds")
    analysis_details = {'Total sentences': totalSentences,
                        'Total Words before preprocess': len(re.findall(r'\w+', text)),
                        'Total Distinct Tokens before preprocess': len(set(re.findall(r'\w+', text))),
                        'Average word/sentence before preprocess': len(re.findall(r'\w+', text)) / totalSentences,
                        'Total Words after preprocess': len(tokens),
                        'Total Distinct Tokens after preprocess': len(set(tokens)),
                        'Average word/sentence after preprocess': len(tokens) / totalSentences,
                        'Total verb count': totalVerbs,
                        'Total adverb count': totalAdverbs,
                        'Total adjective count': totalAdjectives,
                        'Total noun count': totalNouns,
                        'Total emoticons': totalEmoticons,
                        'Total slangs': totalSlangs,
                        'Most popular slangs': d1,
                        'Total elongated words': totalElongated,
                        'Total multi exclamation marks': totalMultiExclamationMarks,
                        'Total multi question marks': totalMultiQuestionMarks,
                        'Total multi stop marks': totalMultiStopMarks,
                        'Total all capitalized words': totalAllCaps,
                        'Most common words': d2,
                        'Most common collocations - bigrams': bigms,
                        'Most common collocations - trigrams': trigms
                        }

    return analysis_details
