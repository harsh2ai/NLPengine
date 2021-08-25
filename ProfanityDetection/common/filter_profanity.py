import spacy
from profanity_filter import ProfanityFilter

nlp = spacy.load('en')
profanity_filter = ProfanityFilter(nlps={'en': nlp})  # reuse spacy Language (optional)
nlp.add_pipe(profanity_filter.spacy_component, last=True)


def filter_profane_words(text):
    result = []

    # Profanity check
    pd = nlp(text)

    # If text passed is profane
    if pd._.is_profane:

        # Iterate through text to get profane word
        for word in text:

            # Check if flag; is_profane is true
            if (word._.is_profane):
                # Filter out the profane word
                result.append({'word': word,
                               'censored': word._.censored,
                               'is_profane': word._.is_profane,
                               'original_profane_word': word._.original_profane_word})
    return result


filter_profane_words("You have got to be fucking kidding me and shit.")
