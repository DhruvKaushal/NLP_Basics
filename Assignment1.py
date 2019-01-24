import nltk
from nltk.book import *

#Question 1
coll5 = text5.collocations()

#Q2
my_sent = ["hello" , "world", "its", "dhruv"]
my_sent = ' '.join(my_sent)
my_sent = my_sent.split(' ')

#Q3
yo = text9.index('sunset')
print(yo)

#Q4
senti = []
senti.append(' '.join(sent1))
senti.append(' '.join(sent2))
senti.append(' '.join(sent3))
senti.append(' '.join(sent4))
senti.append(' '.join(sent5))
senti.append(' '.join(sent6))
senti.append(' '.join(sent7))
senti.append(' '.join(sent8))
words = []
for i in range(len(senti)):
    for word in senti[i].split(' '):
        word = word.lower()
        if word not in words:
            words.append(word)
            
#Q5
s1 =sorted(set([w.lower() for w in text1]))
s2 =sorted([w.lower() for w in set(text1)])

#Q6
x = text2[slice(len(text2)-2, len(text2))]


#Q7
words = []
for i in range(len(text2)):
    for word in text2[i].split(' '):
        if len(word)==4 and word not in words:
            words.append(word)
            
