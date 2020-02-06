from pandas import read_csv

print ("Libraries loaded successfully") 
url = "iris.csv" 
names = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'class'] 
dataset = read_csv(url, names=names) 

# Shows the number of rows and columns and other shape if any of the dataset. 
print ("The shape of the data : ", dataset.shape) 

# Get the first 20 rows of the dataset.  
first_20_rows_dataset = dataset.head(20) 
print(first_20_rows_dataset)

# Get the last 20 rows of the dataset. 
last_20_rows_dataset = dataset.tail(20) 
print(last_20_rows_dataset) 

# To print the summary of the data. 
print (dataset.describe()) 

grouped_data_size = dataset.groupby('class').size() 
print ("The size of grouped data : ")  
print (grouped_data_size)