# MLEngine
### Module Details
**1. Textual Analysis: Social Engineering**
 
```
TextualAnalysis
    |___ EntityRecognition
            |___ common
                |___ get_entity_type.py
            |___ readme.md
            |___ EntityRecognition.py
    |___ GetTextAnalysis
            |___ common
                |___analysis_count.py
                |___negation_analysis.py
                |___spellcheck.py
                |___text_analysis.py
                |___text_cleaning.py
            |___ readme.md
            |___ GetTextAnalysis.py
    |___ LanguageDetection
            |___ common
                |___ detect_lang.py
            |___ LanguageDetection.py
            |___ readme.md
    |___ SentimentAnalysis
            |___ common
                |___ get_sentiment_analysis.py
            |___ SentimentAnalysis.py
            |___ readme.md
    |___ SyntaxAnalysis
            |___ common
                |___ get_syntax_analysis.py
            |___ SyntaxAnalysis.py
            |___ readme.md
    |___ TopicModelling
            |___ common
                |___ get_topic.py
            |___ TopicModelling.py
            |___ readme.md
            
    |___ EmotionDetection
           |___EmotionDetection
           |___setup.sh
           |___readme.md
```
Sub-Modules importance or description as mentioned as follows:

**a**. **GetTextualAnalysis** : Possible statistics that can be collective from session level conversation.The session level conversation, includes set of conversation that happened within a group or between two individuals within a timestamp that's within a session.
```
Sample Output :-

{'count_analysis': {'Total sentences': 100, 
                    'Total Words before preprocess': 38509, 
                    'Total Distinct Tokens before preprocess': 12196, 
                    'Average word/sentence before preprocess': 385.09,
                    'Total Words after preprocess': 978, 
                    'Total Distinct Tokens after preprocess': 603, 
                    'Average word/sentence after preprocess': 9.78, 
                    'Total verb count': 92, 'Total adverb count': 39, 
                    'Total adjective count': 63, 'Total noun count': 98, 
                    'Total emoticons': 22, 
                    'Total slangs': 17, 
                    'Most popular slangs': {'u': 4, 'lol': 3, 'wtf': 2, 'bro': 1, 'y': 1, 'til': 1, 'ugh': 1, 'x': 1, 'idk': 1, 'ur': 1, 'ppl': 1}, 
                    'Total elongated words': 8, 
                    'Total multi exclamation marks': 8, 
                    'Total multi question marks': 3, 
                    'Total multi stop marks': 31, 
                    'Total all capitalized words': 33, 
                    'Most common words': {'atus': 50, 'multistop': 31, 'of': 27, 'get': 9, 'am': 9, 'multiexclam': 8, 'to': 8, 'want': 8, 'know': 7, 'love': 6}, 
                    'Most common collocations - bigrams': None, 
                    'Most common collocations - trigrams': []}}
```
**b. Entity Recognition** : Named-entity recognition (also known as (named) entity identification, entity chunking, and entity extraction) is a Natural Language Processing subtask of information extraction that seeks to locate and classify named entities mentioned in unstructured text into pre-defined categories such as person names, organizations, locations, medical codes, time expressions, quantities, monetary values, percentages, etc.
```
Sample Output:-
{'ner_detected' = [{'entity': 'I-ORG', 'word': '##cie', 'recognition_score': 0.9012304, 'word_index': {'index': 2, 'start_loc': 2, 'end_loc': 5}},
                    {'entity': 'I-LOC', 'word': 'Iran', 'recognition_score': 0.999788, 'word_index': {'index': 2, 'start_loc': 1, 'end_loc': 5}}, 
                    {'entity': 'I-PER', 'word': 'God', 'recognition_score': 0.96704215, 'word_index': {'index': 8, 'start_loc': 26, 'end_loc': 29}}, 
                    {'entity': 'I-ORG', 'word': '##S', 'recognition_score': 0.9556692, 'word_index': {'index': 5, 'start_loc': 6, 'end_loc': 7}}, 
                    {'entity': 'I-PER', 'word': 'Hector', 'recognition_score': 0.99875647, 'word_index': {'index': 9, 'start_loc': 42, 'end_loc': 48}}, 
                    {'entity': 'I-PER', 'word': 'Sant', 'recognition_score': 0.99953884, 'word_index': {'index': 10, 'start_loc': 49, 'end_loc': 53}}, 
                    {'entity': 'I-PER', 'word': '##s', 'recognition_score': 0.9984433, 'word_index': {'index': 11, 'start_loc': 53, 'end_loc': 54}}]
```
**c. Language Detection** : Multiple languages present in text data could be one of the reasons your model behaves strangely.
```
Sample Output:-
{'lang_detection':[{'language_code': 'en', 'language': 'English', 'score': 1.0}, 
                    {'language_code': 'en', 'language': 'English', 'score': 0.857}]

```
**d. Sentiment Analysis** : It is the process of classifying text as either positive, negative, or neutral.
```
Sample Output:-
{'sentiment_analysis': [{'text': '?RT @justinbiebcr: The bigger the better....if you know what I mean ;)', 'label': {'NEGATIVE'}, 'score': 0.9445},
                        {'text': "if my mom went on for the love of ray J or any reality show i'd bee pissed .", 'label': {'NEGATIVE'}, 'score': 0.999}, 
                        {'text': "@BarCough it's enough to make you sick, eh? there's nothing sacred anymore", 'label': {'NEGATIVE'}, 'score': 0.995}, 
                        {'text': 'Hacienda is now level 80 time to get epic gear for her!!!! Oh and maybe some sleep would be good..', 'label': {'NEGATIVE'}, 'score': 0.9182}, 
                        {'text': '"Iran, with its unity and God\'s grace, will punch the arrogance (West) 22nd of Bahman (Feb 11) in a way that will leave them stunned,"', 'label': {'POSITIVE'}, 'score': 0.9804}, 
                        {'text': '@TiffyStarz wtf, where i come from noone likes metal and hardcore, like 5 of my mates max are fully into metal, it sucks, i love metalll :L', 'label': {'POSITIVE'}, 'score': 0.9964}, 
                        {'text': "#4WordsOnObamasHand Don't Say The N-Word", 'label': {'NEGATIVE'}, 'score': 0.9967}, {'text': 'City watchdog in chaos as chief executive Hector Sants resigns just months before general election', 'label': {'NEGATIVE'}, 'score': 0.9974}, 
                        {'text': '@russmarshalek Sold! Would love to be your crazyass big sis -- how could I say no?! Cannot believe I broke or minimally battered my toe --', 'label': {'NEGATIVE'}, 'score': 0.9945}, 
                        {'text': 'i need money! i need new car!!! jesus...somebody please buy my old car :DDD', 'label': {'NEGATIVE'}, 'score': 0.9989}]}
```
**e. Syntax Analysis** : Linguistic Analysis, starting from raw text to syntactic analysis and entity recognition.
```
Sample Output:
{'syntax_analysis': [{'text': '?RT @justinbiebcr: The bigger the better....if you know what I mean ;)', 'per_analysis': {'punct': 18.75, 'pron': 18.75, 'propn': 12.5, 'det': 12.5, 'adj': 12.5, 'verb': 12.5, 'sconj': 6.25, 'sym': 6.25}}, 
                    {'text': "if my mom went on for the love of ray J or any reality show i'd bee pissed .", 'per_analysis': {'noun': 36.84, 'det': 15.79, 'verb': 10.53, 'adp': 10.53, 'sconj': 5.26, 'pron': 5.26, 'adv': 5.26, 'cconj': 5.26, 'punct': 5.26}}, 
                    {'text': "@BarCough it's enough to make you sick, eh? there's nothing sacred anymore", 'per_analysis': {'pron': 25.0, 'adj': 18.75, 'verb': 12.5, 'sym': 6.25, 'propn': 6.25, 'aux': 6.25, 'part': 6.25, 'punct': 6.25, 'cconj': 6.25, 'adv': 6.25}}, 
                    {'text': 'Hacienda is now level 80 time to get epic gear for her!!!! Oh and maybe some sleep would be good..', 'per_analysis': {'noun': 18.18, 'aux': 13.64, 'adv': 9.09, 'adj': 9.09, 'punct': 9.09, 'propn': 4.55, 'num': 4.55, 'part': 4.55, 'verb': 4.55, 'adp': 4.55, 'pron': 4.55, 'intj': 4.55, 'cconj': 4.55, 'det': 4.55}}, 
                    {'text': '"Iran, with its unity and God\'s grace, will punch the arrogance (West) 22nd of Bahman (Feb 11) in a way that will leave them stunned,"', 'per_analysis': {'punct': 25.71, 'propn': 14.29, 'noun': 14.29, 'adp': 8.57, 'pron': 8.57, 'verb': 8.57, 'aux': 5.71, 'det': 5.71, 'cconj': 2.86, 'part': 2.86, 'num': 2.86}}, 
                    {'text': '@TiffyStarz wtf, where i come from noone likes metal and hardcore, like 5 of my mates max are fully into metal, it sucks, i love metalll :L', 'per_analysis': {'punct': 18.18, 'pron': 15.15, 'noun': 15.15, 'verb': 12.12, 'adp': 12.12, 'propn': 9.09, 'sconj': 3.03, 'cconj': 3.03, 'adj': 3.03, 'num': 3.03, 'aux': 3.03, 'adv': 3.03}}, 
                    {'text': "#4WordsOnObamasHand Don't Say The N-Word", 'per_analysis': {'noun': 28.57, 'aux': 14.29, 'part': 14.29, 'verb': 14.29, 'det': 14.29, 'propn': 14.29}}, {'text': 'City watchdog in chaos as chief executive Hector Sants resigns just months before general election', 'per_analysis': {'noun': 26.67, 'propn': 20.0, 'adp': 20.0, 'adj': 20.0, 'verb': 6.67, 'adv': 6.67}}, 
                    {'text': '@russmarshalek Sold! Would love to be your crazyass big sis -- how could I say no?! Cannot believe I broke or minimally battered my toe --', 'per_analysis': {'verb': 21.43, 'punct': 14.29, 'aux': 14.29, 'pron': 14.29, 'noun': 10.71, 'adv': 7.14, 'propn': 3.57, 'part': 3.57, 'adj': 3.57, 'intj': 3.57, 'cconj': 3.57}}, 
                    {'text': 'i need money! i need new car!!! jesus...somebody please buy my old car :DDD', 'per_analysis': {'pron': 22.22, 'verb': 16.67, 'noun': 16.67, 'punct': 16.67, 'adj': 11.11, 'propn': 5.56, 'intj': 5.56, 'sym': 5.56}}]}
```

**f. Topic Modeling** : Topic Modeling is a technique to understand and extract the hidden topics from large volumes of text.

```
Sample Output:
{'topic_analysis': [{'text': '?RT @justinbiebcr: The bigger the better....if you know what I mean ;)',
                            'topics': ['better', 'bigger', 'justinbiebcr', 'know', 'mean'], 
                            'topic_dist': {'better-bigger': 3, 'better-justinbiebcr': 9, 'better-know': 6, 'better-mean': 5, 'bigger-justinbiebcr': 9, 'bigger-know': 6, 'bigger-mean': 6, 'justinbiebcr-know': 11, 'justinbiebcr-mean': 11, 'know-mean': 4}}, 
                    {'text': "if my mom went on for the love of ray J or any reality show i'd bee pissed .", 
                            'topics': ['go', 'love', 'piss', 'realiti'], 
                            'topic_dist': {'go-love': 3, 'go-piss': 4, 'go-realiti': 7, 'love-piss': 4, 'love-realiti': 6, 'piss-realiti': 6}}, 
                    {'text': "@BarCough it's enough to make you sick, eh? there's nothing sacred anymore", 
                            'topics': ['anymor', 'barcough', 'sacr', 'sick'], 
                            'topic_dist': {'anymor-barcough': 7, 'anymor-sacr': 5, 'anymor-sick': 6, 'barcough-sacr': 6, 'barcough-sick': 7, 'sacr-sick': 2}}, 
                    {'text': 'Hacienda is now level 80 time to get epic gear for her!!!! Oh and maybe some sleep would be good..', 
                            'topics': ['epic', 'gear', 'good', 'hacienda', 'level', 'mayb', 'sleep', 'time'], 
                            'topic_dist': {'epic-gear': 4, 'epic-good': 4, 'epic-hacienda': 7, 'epic-level': 4, 'epic-mayb': 4, 'epic-sleep': 5, 'epic-time': 4, 'gear-good': 3, 'gear-hacienda': 7, 'gear-level': 4, 'gear-mayb': 4, 'gear-sleep': 4, 'gear-time': 4, 'good-hacienda': 7, 'good-level': 5, 'good-mayb': 4, 'good-sleep': 5, 'good-time': 4, 'hacienda-level': 7, 'hacienda-mayb': 7, 'hacienda-sleep': 7, 'hacienda-time': 7, 'level-mayb': 5, 'level-sleep': 3, 'level-time': 4, 'mayb-sleep': 5, 'mayb-time': 4, 'sleep-time': 4}}, 
                    {'text': '"Iran, with its unity and God\'s grace, will punch the arrogance (West) 22nd of Bahman (Feb 11) in a way that will leave them stunned,"', 
                            'topics': ['arrog', 'bahman', 'grace', 'iran', 'leav', 'punch', 'stun', 'uniti', 'west'], 
                            'topic_dist': {'arrog-bahman': 5, 'arrog-grace': 4, 'arrog-iran': 4, 'arrog-leav': 5, 'arrog-punch': 5, 'arrog-stun': 5, 'arrog-uniti': 5, 'arrog-west': 5, 'bahman-grace': 6, 'bahman-iran': 4, 'bahman-leav': 5, 'bahman-punch': 6, 'bahman-stun': 5, 'bahman-uniti': 6, 'bahman-west': 6, 'grace-iran': 3, 'grace-leav': 4, 'grace-punch': 4, 'grace-stun': 5, 'grace-uniti': 5, 'grace-west': 5, 'iran-leav': 3, 'iran-punch': 5, 'iran-stun': 3, 'iran-uniti': 5, 'iran-west': 4, 'leav-punch': 5, 'leav-stun': 4, 'leav-uniti': 5, 'leav-west': 3, 'punch-stun': 4, 'punch-uniti': 4, 'punch-west': 5, 'stun-uniti': 5, 'stun-west': 4, 'uniti-west': 4}}]}
 ```
 
**2. Insult Detection Model**

It is almost impossible  to engage in online conversations without witnessing toxic behavior like unwarranted  harassment or disrespect. 
This module will be dealing with toxicity online and curbing harassment within a social space or a group.

```
Aim: The objective of this module is to develop an NLP model,
 that is capable of automatically identifying & filtering out 
 abusive/toxic behavior such as :
   
    - personal abuse, 
    - insults, 
    - bullying. 

within the  conversations/comments on platforms to ensure 
    - a safe &
    - secure environment for the end users

InsultDetection
    |__ Deeppalov_InsultDetection.py
    |__readme.md
    |__setup.sh : run script to install models and required libraries
```

```
Sample Output:
{'insult_detection':[{'?RT @justinbiebcr: The bigger the better..shit....if you know what I mean ;)': {'Not Insult'}},
                    {"if my mom went on for the love of ray J or any reality show i'd bee pissed .": {'Not Insult'}},
                    {"@BarCough it's enough to make you sick, eh? there's nothing sacred anymore": {'Not Insult'}},
                    {'Hacienda is now level 80 time to get epic gear for her!!!! Oh and maybe some sleep would be good..': {'Not Insult'}}, 
                    {'"Iran, with its unity and God\'s grace, will punch the arrogance (West) 22nd of Bahman (Feb 11) in a way that will leave them stunned,"': {'Not Insult'}}, 
                    {'@russmarshalek Sold! Would love to be your crazyass big sis -- how could I say no?! Cannot believe I broke or minimally battered my toe --': {'Not Insult'}}, 
                    {'You are such an idiot and dumbass.':{'Insult'},
                    {'i need money! i need new car!!! jesus...somebody please buy my old car :DDD': {'Not Insult'}}]}

```

**3. Personal Information Exchange Detection**

    - any type of PI shared over the platform during a conversation
    - For example, detection of:- 
        * personal email, 
        * address,
        * account details, etc.

**4. Script Detection**

    - Sharing code on conversational platform
    - marked as potential threat to company's policies
    - possible leak of confidential information or any data

**5. Profanity Detection**

    - to check for profanity or offensive language in strings
    - filter out profane words


**6. Emotion Detection Model**

The  conversations can have different types of emotions here we are trying to detect emotions.


```
Sample Output :-
{"emotion is": " anger"}
```

---


### Directory Structure

```
MLEngine
    |___TextualAnalysis/
    |___InsultDetection/
    |___PIIDetection/
    |___ScriptDetection/
    |___JNotebooks/
    |___MLCommon/ : all common scripts 
    |___MLData/ : required data
        |___TextAnalysisData/
            |___corporaForSpellCorrection.txt
            |___slang.txt
            |___ss-twitterfinal.txt
        |__HarassmentData
            |__allNeg.csv
            |__nlpdatasqupdated.csv
            |__subreditupdated.csv
    |___MLResources/ : path to save trained models
    |__ GetTextualAnalysis.py
    |___README.md
    |___requirments.txt
    |___ .gitignore : added extension of files not to push to git  
    |___main.py
```

### Testing the APIs:
1. Run "uvicorn main:app"
2. Visit to 127.0.0.1:8000/docs for the documentation, to check all the endpoints, their parameters, etc.

```
---
**Author - _`Shivani Tyagi (Data Scientist)
             - shivani.tg94@yahoo.com`_**

**Copyright issued to @Scanta Inc.**
