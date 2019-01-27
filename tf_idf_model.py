import nltk
import re
import heapq
import numpy as np

#Text modelling uaing bag of words
#Building the BOW model
text = """Beans. I was trying to explain to somebody as we were flying in, that's corn. 
That's beans. And they were very impressed at my agricultural knowledge. Please give it 
up for Amaury once again for that outstanding introduction. I have a bunch of good friends 
here today, including somebody who I served with, who is one of the finest senators in 
the country, and we're lucky to have him, your Senator, Dick Durbin is here. I also noticed, 
by the way, former Governor Edgar here, who I haven't seen in a long time, and somehow he 
has not aged and I have. And it's great to see you, Governor. I want to thank President 
Killeen and everybody at the U of I System for making it possible for me to be here today. 
And I am deeply honored at the Paul Douglas Award that is being given to me. He is somebody 
who set the path for so much outstanding public service here in Illinois.
 Now, I want to start by addressing the elephant in the room. I know people are still 
 wondering why I didn't speak at the commencement."""
 
dataset = nltk.sent_tokenize(text)
for i in range(len(dataset)):
    dataset[i] = dataset[i].lower()
    dataset[i] = re.sub(r'\W', ' ', dataset[i])
    dataset[i] = re.sub(r'\s+',' ', dataset[i])
    
#Creating the histograms
word2count = {}
for data in dataset:
    words = nltk.word_tokenize(data)
    for word in words:
        if word not in word2count.keys():
            word2count[word] = 1
        else:
            word2count[word] += 1
            
freq_words = heapq.nlargest(100, word2count, key=word2count.get)

#IDF Matrix

word_idfs = {}
for word in freq_words:
    doc_count = 1
    for data in dataset:
        if word in nltk.word_tokenize(data):
            doc_count +=1
        word_idfs[word] = np.log((len(dataset)/doc_count))

#TF matrix
tf_matrix = {}
for word in freq_words:
    doc_tf = []
    for data in dataset:
        frequency = 0
        for w in nltk.word_tokenize(data):
            if word == w:
                frequency += 1
        tf_word = frequency/len(nltk.word_tokenize(data))
        doc_tf.append(tf_word)
    tf_matrix[word] = doc_tf
    
