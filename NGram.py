import random

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
    

