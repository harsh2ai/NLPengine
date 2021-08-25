""" Copyright 2021, Scanta Inc., All rights reserved. """

from nltk.corpus import wordnet


### Replace Negations Begin

def replace(word, pos=None):
    # Creates a set of all antonyms for the word and if there is only one antonym, it returns it
    antonyms = set()
    for syn in wordnet.synsets(word, pos=pos):
        for lemma in syn.lemmas():
            for antonym in lemma.antonyms():
                antonyms.add(antonym.name())
    if len(antonyms) == 1:
        return antonyms.pop()
    else:
        return None


def replaceNegations(text):
    # Finds "not" and antonym for the next word and if found,
    # replaces not and the next word with the antonym
    i, l = 0, len(text)
    words = []
    while i < l:
        word = text[i]
        if word == 'not' and i + 1 < l:
            ant = replace(text[i + 1])
            if ant:
                words.append(ant)
                i += 2
                continue
        words.append(word)
        i += 1
    return words
