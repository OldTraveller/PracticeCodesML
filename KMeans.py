from sklearn.feature_extraction.text import CountVectorizer
from sklearn.datasets import fetch_20newsgroups 
from nltk.corpus import names
from nltk.stem import WordNetLemmatizer
from sklearn.cluster import KMeans 
import matplotlib.pyplot as plt 

def letters_only(chars): 
    return chars.isalpha() 

cv = CountVectorizer(stop_words="english", max_features=500) 
groups = fetch_20newsgroups() 
cleaned = [] 
all_names = set(names.words()) 
lemmatizer = WordNetLemmatizer() 

for post in groups.data: 
    cleaned.append(' '.join([
        lemmatizer.lemmatize(word.lower())
        for word in post.split()
        if letters_only(word) and 
        word not in all_names
    ]))

# Fit the transform 
transformed = cv.fit_transform(cleaned) 

km = KMeans(n_clusters=20) 

print ("Training ...")
km.fit(transformed) 

labels = groups.target 
plt.scatter(labels, km.labels_)
# To name the X and Y axis 
plt.xlabel('NewsGroup') 
plt.ylabel('Cluster') 
plt.show() 
