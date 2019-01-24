import nltk
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

