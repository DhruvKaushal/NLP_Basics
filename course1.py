

import re
sent = "Hello there how are you"
re.match(r"Hell", sent)

#Substituting
sent = "I love avengers"
print(re.sub("avengers", "Justice league", sent))
print(sent)