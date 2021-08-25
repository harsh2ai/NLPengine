""" Copyright 2021, Scanta Inc., All rights reserved. """

import re

from nltk.corpus import wordnet

# Replaces contractions from a string to their equivalents
contraction_patterns = [(r'won\'t', 'will not'), (r'can\'t', 'cannot'), (r'i\'m', 'i am'), (r'ain\'t', 'is not'),
                        (r'(\w+)\'ll', '\g<1> will'), (r'(\w+)n\'t', '\g<1> not'),
                        (r'(\w+)\'ve', '\g<1> have'), (r'(\w+)\'s', '\g<1> is'), (r'(\w+)\'re', '\g<1> are'),
                        (r'(\w+)\'d', '\g<1> would'), (r'&', 'and'), (r'dammit', 'damn it'), (r'don\'t', 'do not'),
                        (r'wont', 'will not')]


def removeUnicode(text):
    # Removes unicode strings like "\u002c" and "x96"
    # Pass regex pattern to remove unicode strings from the text
    text = re.sub(r'(\\u[0-9A-Fa-f]+)', r'', text)
    text = re.sub(r'[^\x00-\x7f]', r'', text)
    return text


def replaceURL(text):
    # Replaces url address with "url"
    # Pass possible pattern for url
    text = re.sub('((www\.[^\s]+)|(https?://[^\s]+))', 'url', text)
    text = re.sub(r'#([^\s]+)', r'\1', text)
    return text


def replaceAtUser(text):
    # Replaces "@user" with "atUser"
    # Username modification
    text = re.sub('@[^\s]+', 'atUser', text)
    return text


def removeHashtagInFrontOfWord(text):
    # Pattern to detect hashtag in given string
    # Removes hashtag in front of a word
    text = re.sub(r'#([^\s]+)', r'\1', text)
    return text


def removeNumbers(text):
    # Removes integers
    text = ''.join([i for i in text if not i.isdigit()])
    return text


def replaceMultiExclamationMark(text):
    # Replaces repetitions of exclamation marks
    text = re.sub(r"(\!)\1+", ' multiExclamation ', text)
    return text


def replaceMultiQuestionMark(text):
    # Replaces repetitions of question marks
    text = re.sub(r"(\?)\1+", ' multiQuestion ', text)
    return text


def replaceMultiStopMark(text):
    # Replaces repetitions of stop marks
    text = re.sub(r"(\.)\1+", ' multiStop ', text)
    return text


def replaceContraction(text):
    patterns = [(re.compile(regex), repl) for (regex, repl) in contraction_patterns]
    for (pattern, repl) in patterns:
        (text, count) = re.subn(pattern, repl, text)
    return text


def replaceElongated(word):
    # Replaces an elongated word with its basic form,
    # unless the word exists in the lexicon
    repeat_regexp = re.compile(r'(\w*)(\w)\2(\w*)')
    repl = r'\1\2\3'
    if wordnet.synsets(word):
        return word
    repl_word = repeat_regexp.sub(repl, word)
    if repl_word != word:
        return replaceElongated(repl_word)
    else:
        return repl_word


def removeEmoticons(text):
    # Removes emoticons from text
    text = re.sub(
        ':\)|;\)|:-\)|\(-:|:-D|=D|:P|xD|X-p|\^\^|:-*|\^\.\^|\^\-\^|\^\_\^|\,-\)|\)-:|:\'\(|:\(|:-\(|:\S|T\.T|\.\_\.|:<|:-\S|:-<|\*\-\*|:O|=O|=\-O|O\.o|XO|O\_O|:-\@|=/|:/|X\-\(|>\.<|>=\(|D:',
        '', text)
    return text


def addNotTag(text):
    # Finds "not,never,no" and adds the tag NEG_ to all words that follow until the next punctuation #
    transformed = re.sub(r'\b(?:not|never|no)\b[\w\s]+[^\w\s]',
                         lambda match: re.sub(r'(\s+)(\w+)', r'\1NEG_\2', match.group(0)),
                         text,
                         flags=re.IGNORECASE)
    return transformed


def addCapTag(word):
    # Finds a word with at least 3 characters capitalized and adds the tag ALL_CAPS_ #
    if (len(re.findall("[A-Z]{3,}", word))):
        word = word.replace('\\', '')
        transformed = re.sub("[A-Z]{3,}", "ALL_CAPS_" + word, word)
        return transformed
    else:
        return word
