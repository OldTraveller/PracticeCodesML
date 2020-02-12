import glob 
import os 
from nltk.corpus import names 
from nltk.stem import WordNetLemmatizer 
from sklearn.feature_extraction.text import CountVectorizer 
import numpy as np 

emails, labels = [], [] 
lemmatizer = WordNetLemmatizer() 
spam_file_path = 'enron1/spam/'
ham_file_path = 'enron1/ham/' 
all_names = set(names.words()) 
cv = CountVectorizer(stop_words='english', max_features=500)
########################################################################
#                               METHODS                                #
########################################################################
def letters_only(chars): 
    return chars.isalpha() 

def clean_text(docs): 
    cleaned_docs = []
    for doc in docs: 
        cleaned_docs.append(' '.join([lemmatizer.lemmatize(word.lower()) for word in doc.split() if letters_only(word) and word not in all_names]))
    return cleaned_docs

def get_label_index(labels): 
    from collections import defaultdict
    label_index = defaultdict(list) 
    for index, label in enumerate(labels): 
        label_index[label].append(index) 
    return label_index

def get_prior(label_index): 
    prior = { label: len(index) for label, index in label_index.iteritems() }
    total_count = sum(prior.values()) 
    for label in prior: 
        prior[label] /= float(total_count) 
    return prior

def get_likelihood(term_document_matrix, label_index, smoothing=0):
    likelihood[label] = {} 
    
########################################################################
for file_name in glob.glob(os.path.join(spam_file_path, '*.txt')):
    with open(file_name, 'r', encoding='ISO-8859-1') as infile: 
        emails.append(infile.read())
        labels.append(1) 

for file_name in glob.glob(os.path.join(ham_file_path, '*.txt')): 
    with open (file_name, 'r', encoding='ISO-8859-1') as infile: 
        emails.append(infile.read()) 
        labels.append(0) 
########################################################################

cleaned_emails = clean_text(emails) 

print ("Total Emails Cleaned : ", len(cleaned_emails)) 

# Till here we have the cleaned data. We removed the stop words. We lemmatized the text. 
# And removed all the unnecessary stop words .
term_docs = cv.fit_transform(cleaned_emails) 
print ("Term Docs 0") 
print (term_docs[0]) 

print ("Feature Names") 
feature_names = cv.get_feature_names() 
print (feature_names[480]) 

# Get the label index 
label_index = get_label_index(labels) 

prior = get_prior(label_index) 
prior ("PRIOR") 
prior (prior) 



