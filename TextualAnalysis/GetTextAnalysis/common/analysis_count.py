""" Copyright 2021, Scanta Inc., All rights reserved. """

import re
from functools import partial

import nltk

# Constant variables added
with open('MLData/TextAnalysisData/slang.txt') as file:
    slang_map = dict(map(str.strip, line.partition('\t')[::2])
                     for line in file if line.strip())

slang_words = sorted(slang_map, key=len, reverse=True)  # longest first for regex
regex = re.compile(r"\b({})\b".format("|".join(map(re.escape, slang_words))))
replaceSlang = partial(regex.sub, lambda m: slang_map[m.group(1)])


def countMultiExclamationMarks(text):
    # Replaces repetitions of exclamation marks
    return len(re.findall(r"(\!)\1+", text))


def countMultiQuestionMarks(text):
    # Count repetitions of question marks
    return len(re.findall(r"(\?)\1+", text))


def countMultiStopMarks(text):
    # Count repetitions of stop marks
    return len(re.findall(r"(\.)\1+", text))


def countElongated(text):
    # Input: a text, Output: how many words are elongated
    regex_pattern = re.compile(r"(.)\1{2}")
    return len([word for word in text.split() if regex_pattern.search(word)])


def countSlang(text):
    # Input: a text, Output: how many slang words and a list of found slangs
    slangCounter = 0
    slangsFound = []
    try:
        tokens = nltk.word_tokenize(text)
    except:
        nltk.download('punkt')
        tokens = nltk.word_tokenize(text)
    for word in tokens:
        if word in slang_words:
            slangsFound.append(word)
            slangCounter += 1
    return slangCounter, slangsFound


def countAllCaps(text):
    # Input: a text, Output: how many words are all caps #
    return len(re.findall("[A-Z0-9]{3,}", text))


def countEmoticons(text):
    # Input: a text, Output: how many emoticons
    return len(re.findall(
        ':\)|;\)|:-\)|\(-:|:-D|=D|:P|xD|X-p|\^\^|:-*|\^\.\^|\^\-\^|\^\_\^|\,-\)|\)-:|:\'\(|:\(|:-\(|:\S|T\.T|\.\_\.|:<|:-\S|:-<|\*\-\*|:O|=O|=\-O|O\.o|XO|O\_O|:-\@|=/|:/|X\-\(|>\.<|>=\(|D:',
        text))
