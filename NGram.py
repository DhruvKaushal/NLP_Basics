import random

# Sample data
text = """Global warming or climate change has become a worldwide concern. It is 
gradually developing into an unprecedented environmental crisis evident in melting
 glaciers, changing weather patterns, rising sea levels, floods, cyclones and 
 droughts. Global warming implies an increase in the average temperature of the 
 Earth due to entrapment of greenhouse gases in the earth’s atmosphere."""
 
n = 7

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