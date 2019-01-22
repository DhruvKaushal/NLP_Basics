import nltk
from nltk import PorterStemmer
para = "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum."

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
    