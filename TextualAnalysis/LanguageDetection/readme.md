### LANGUAGE DETECTION MODEL

> Multiple languages present in text data could be one of the reasons your model behaves strangely.

Requirements:-
1. install the spacy-langdetect & 
2. install spacy 
3. predifened language-full-form dictionary: to map language code to full form

### Work Flow of the Language Detection

```
1. Download the best-matching default model and create a shortcut link.
2. Add LanguageDetector() function and model to NLP pipeline.
3. Pass the text data into the pipeline for language detection.
4. Store the detected language and accuracy in the detect_language variable.
```

### Application of language detection

```
1. Find out bias in text data based on the languages.
2. Can classify the article based on the different languages.
3. Language is generally associated with the region. This method helps you to classify the article based on languages.
4. Can use this method in the language translation model.
5. Can use it in data cleaning and data manipulation processes.
```
### Model output

```
Output: 
Language detected: {'language_code': 'de', 'language': 'German', 'score': 1.0}

```
---
**Author - _`Shivani Tyagi (Data Scientist)
             - shivani.tg94@yahoo.com`_**

**Copyright issued to @Scanta Inc.**
