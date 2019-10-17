# coding: utf-8
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
 
text = 'Dans ce tutoriel, j\'apprends NLTK. c\'est intéressant.'
stop_words = set(stopwords.words('french'))
words = word_tokenize(text)
 
new_sentence = []
 
for word in words:
    if word not in stop_words:
        new_sentence.append(word)
 
print(new_sentence)