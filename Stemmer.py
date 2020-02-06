from nltk.stem.porter import PorterStemmer 
from nltk.stem import WordNetLemmatizer 

# Using porter stemmer
porter_stemmer = PorterStemmer() 
stem_learning = porter_stemmer.stem("Learning") 
print (stem_learning) 
machine_learning = porter_stemmer.stem("doing") 
print (machine_learning) 
machines = porter_stemmer.stem("machines") 
print (machines) 

# Using lemmatization 
lemmatizer = WordNetLemmatizer() 
print (lemmatizer.lemmatize("Machines")) 
print (lemmatizer.lemmatize("grinding")) 
print (lemmatizer.lemmatize("went")) 



