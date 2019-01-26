import nltk
import re
import heapq
from nltk import PorterStemmer
para = "Thor is played by Chris hemsworth"

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


#Removal of stopwords
from nltk.corpus import stopwords
sentence = nltk.sent_tokenize(para)
for i in range(len(sentence)):
    words = nltk.word_tokenize(sentence[i])
    newwords = [word for word in words if word not in stopwords.words('english')]
    sentence[i] = ' '.join(newwords)
    
#Tagged words
sentence = nltk.sent_tokenize(para)
tagged_words = nltk.pos_tag(sentence)
word_tags = []
for tw in tagged_words:
    word_tags.append(tw[0] + '_' + tw[1])
tagged_para = ' '.join(word_tags)

#Named entity recognition
words = nltk.word_tokenize(para)
tagged_words = nltk.pos_tag(words)
named_ent = nltk.ne_chunk(tagged_words)
named_ent.draw()

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