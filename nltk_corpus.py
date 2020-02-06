from nltk import pos_tag 
from nltk import word_tokenize 

text = word_tokenize("Hey there I am Abhishek Kumar Rai")
pos = pos_tag(text) 

for tuple in pos: 
    print (tuple[0], ":", tuple[1]) 

