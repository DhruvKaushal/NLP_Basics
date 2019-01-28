

import re
sent = "Hello there how are you"
re.match(r"Hell", sent)

#Substituting
sent = "I love avengers"
print(re.sub("avengers", "Justice league", sent))
print(sent)

#Stemming
sentence = nltk.sent_tokenize(para)
stemmer = PorterStemmer()

for i in range(len(sentence)):
    words = nltk.word_tokenize(sentence[i])
    newwords = [stemmer.stem(word) for word in words]
    sentence[i] = ' '.join(newwords)
    
#lemmatization
from nltk.stem import WordNetLemmatizer
sentenceL = nltk.sent_tokenize(para)
lemmatizer = WordNetLemmatizer()
for i in range(len(sentenceL)):
    wordsL = nltk.word_tokenize(sentenceL[i])
    newwordsL = [lemmatizer.lemmatize(word) for word in wordsL]
    sentenceL[i] = ' '.join(newwordsL)
