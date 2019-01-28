import random
import nltk
# Sample data
text = """Global warming or climate change has become a worldwide concern. It is 
gradually developing into an unprecedented environmental crisis evident in melting
 glaciers, changing weather patterns, rising sea levels, floods, cyclones and 
 droughts. Global warming implies an increase in the average temperature of the 
 Earth due to entrapment of greenhouse gases in the earth’s atmosphere."""
 
n = 3

#Create ngrams(trigram)
ngrams = {}
for i in range(len(text)-n):
    gram = text[i:i+n]
    if gram not in ngrams.keys():
        ngrams[gram] = []
    ngrams[gram].append(text[i+n])
    

#Testing our N gram model
currentGram = text[0:n]
result = currentGram
for i in range(100):
    if currentGram not in ngrams.keys():
        break
    possibility = ngrams[currentGram]
    nextItem = possibility[random.randrange(len(possibility))]
    result += nextItem
    currentGram = result[len(result)-n:len(result)]
print(result)

#Ngram model by word
ngrams = {}
words = nltk.word_tokenize(text)
for i in range(len(words)-n):
    gram = ' '.join(words[i:i+n])
    if gram not in ngrams.keys():
        ngrams[gram] = []
    ngrams[gram].append(words[i+n])
    
currentGram = ' '.join(words[0:n])
result = currentGram
for i in range(30):
    if currentGram not in ngrams.keys():
        break
    possibility = ngrams[currentGram]
    nextItem = possibility[random.randrange(len(possibility))]
    result +=' ' + nextItem
    rwords = nltk.word_tokenize(result)
    currentGram = ' '.join(rwords[len(rwords)-n:len(rwords)])
    
print(result)