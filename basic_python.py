# VARIABLE DECLARATION 
something = 10 

# IF, ELSIF AND ELSE 
if something == 10: 
    print ("Something is : ", something)  
elif something == 11: 
    print ("Something is 11") 
else: 
    print ("Something has some other value!") 

# LIST 
num = [1,2,3,4,5,6] 
print (min(num)) 
print (max(num)) 
print (sum(num)) 

num_vowels = 0 
string = "My name is abhshek" 

# FUNCTIONS 
def is_vowel(c): 
    if c in 'aeiouAEIOU': 
        return True 
    return False

# FOR LOOP 
for char in string: 
    if is_vowel(char): 
        num_vowels = num_vowels + 1
print ("Total vowels : ", num_vowels) 

# DICTIONARY 
dict = {
    "NAME" : "ABHISHEK KUMAR RAI", 
    "COLLEGE" : "UVCE"
}
print (dict.get("NAME")) 
print (dict.get("COLLEGE")) 
dict["NAME"] = "ASDFASDF"
print (dict.get("NAME")) 
print (dict.get("COLLEGE")) 

# SET IN PYTHON. DUPLICATE ELEMENTS NOT THERE. 
set_var = set() 
for i in range (1, 11): 
    set_var.add(i) 
print (set_var) 