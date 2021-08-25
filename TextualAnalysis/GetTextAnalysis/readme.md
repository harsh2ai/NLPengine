# Text Analysis : Scoial Engineering

### Text Analysis Techniques in Python 

Most of these techniques are generic and can be used in various applications. 
They are as follows :
```
 1. Remove Unicode Strings and Noise
 2. Replace URLs, User Mentions and Hashtags
 3. Replace Slang and Abbreviations
 4. Replace Contractions
 5. Remove Numbers
 6. Replace Repetitions of Punctuation
 7. Replace Negations with Antonyms
 8. Remove Punctuation
 9. Handling Capitalized Words
 10. Lowercase
 11. Remove Stopwords
 12. Replace Elongated Words
 13. Spelling Correction
 14. Part of Speech Tagging
 15. Lemmatization
 16. Stemming
 ```
---
This scripts also prints some statistics for the text file like: 

- Total Sentences
- Total Words before and after preprocess
- Total Unique words before and after preprocess
- Average Words per Sentence before and after preprocess
- Total Run time
- Total Emoticons found
- Total Slangs and Abbreviations found
- Most Common Slangs and Abbreviations and plots them
- Total Elongated words
- Total multi Exclamation
- Question and stop marks
- Total All Capitalized words
- Most Common words and plots them and most common bigram and trigram collocations

---
### Resources Used

The text file that is used here is a sample (2000 tweets) of the SS-Twitter dataset.

The file "text_analysis.py" includes many comments and in order to use a technique you have to uncomment the appropriate line/lines. The initial script uses all techniques. So if you want to use only specific techniques, comment out the others.

```
Output:
Starting preprocess..

Total sentences:  100

Total Words before preprocess:  38509
Total Distinct Tokens before preprocess:  12196
Average word/sentence before preprocess:  385.09

Total Words after preprocess:  978
Total Distinct Tokens after preprocess:  603
Average word/sentence after preprocess:  9.78

Total verb count:  92
Total adverb count:  39
Total adjective count:  63
Total noun count:  98

Total run time:  15.50177788734436  seconds

Total emoticons:  22

Total slangs:  17 
u        4
lol      3
wtf      2
bro      1
y        1
til      1
ugh      1
x        1
idk      1
ur       1
ppl      1

Total elongated words:  8
Total multi exclamation marks:  8
Total multi question marks:  3
Total multi stop marks:  31
Total all capitalized words:  33

Most common words
Word    Count
atus     50
multistop        31
of       27
get      9
am       9
multiexclam      8
to       8
want     8
know     7
love     6

Most common collocations (bigrams)
[('of', 'atus')]

Most common collocations (trigrams)
[]

```
---
**Author - _`Shivani Tyagi (Data Scientist)
             - shivani.tg94@yahoo.com`_**

**Copyright issued to @Scanta Inc.**