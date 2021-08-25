### Syntax Analysis : Linguistic Analysis
Starting from raw text to syntactic analysis and entity recognition.

### Resources
> **NLPStanza** : Stanza is a Python natural language analysis package. It contains tools, which can be used in a pipeline, to convert a string containing human language text into lists of sentences and words, to generate base forms of those words, their parts of speech and morphological features, to give a syntactic structure dependency parse, and to recognize named entities.

### Pipeline Usage
1. Install required package

    ``pip install stanza``
   
2. Download required model

    > import stanza
   
    > stanza.download('en')
   
3. Model Output

   ```
   Text passed: I want to change my password.Can you help?
   Analysis : {'pron': 30.0, 'verb': 30.0, 'part': 10.0, 'noun': 10.0, 'punct': 10.0, 'aux': 10.0}
   ```
---
**Author -  `Shivani Tyagi (Data Scientist)
             - shivani.tg94@yahoo.com`**

**Copyright issued to @Scanta Inc.**