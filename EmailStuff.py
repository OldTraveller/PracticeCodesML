import glob 
import os 
from nltk.corpus import names 
from nltk.stem import WordNetLemmatizer 

emails, labels = [], [] 
lemmatizer = WordNetLemmatizer() 
spam_file_path = 'enron1/spam/'
ham_file_path = 'enron1/ham/' 
all_names = set(names.words()) 
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

for i in range(0, 5): 
    print (cleaned_emails[i]) 
    print ("########################################################################")


