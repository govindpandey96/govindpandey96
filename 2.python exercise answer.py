#!/usr/bin/env python
# coding: utf-8

# # Python Statements 

# ### Use for, .split() and if to create a statement that will print out the words that start with 's':

# In[14]:


st = 'Print only the words that start with s in this sentence'


# In[18]:


#code here
#String to be splitted
St = 'shyam and sita love eachother'

#Split the string on blank characters
List = St.split()

#for each element in the list, if it starts with 'm' then print it
for s in List:
    if s.startswith('s'):
        print(s)


# ### Use range() to print out all even numbers from 0 to 50

# In[8]:


# Code Here
for i in range(0,50,2):
    print(i)


# ### Use a List Comprehension to create a list of all the numbers between 1 and 50 that are divisible by 3

# In[16]:


#code here
a = range(1,50)

mylist = [x for x in range(50) if x%3==0] 


print(mylist)


 


# ### Go through the string below and if the length of a word is even print 'even!'

# In[13]:


st = 'Print every word in this sentence that has an even number of letters'


# In[6]:


#code here
# Python3 program to print 
#  even length words in a string 
  
def printWords(s):
      
    # split the string 
    s = s.split(' ') 
      
    # iterate in words of string 
    for word in s: 
          
        # if length is even 
        if len(word)%2==0:
            print(word) 
  
  
# Driver Code 
s = " i am Govind" 
printWords(s) 


# ### Write a program that prints the integers from 1 to 100. But for multiples of three print 'Fizz' instead of the number, and for the multiples of five print 'Buzz'. For numbers which are multiples of both three and five print 'FizzBuzz'.

# In[7]:


#code here
# Python program to print Fizz Buzz
 
# Loop for 100 times i.e. range
for fizzbuzz in range(100):
 
    # Number divisible by 15,(divisible
    # by both 3 & 5), print 'FizzBuzz'
    # in place of the number
    if fizzbuzz % 15 == 0:
        print("FizzBuzz")                                        
        continue
 
    # Number divisible by 3, print 'Fizz'
    # in place of the number
    elif fizzbuzz % 3 == 0:    
        print("Fizz")                                        
        continue
 
    # Number divisible by 5,
    # print 'Buzz' in
    # place of the number
    elif fizzbuzz % 5 == 0:        
        print("Buzz")                                    
        continue
 
    # Print numbers
    print(fizzbuzz)


# ### Use List Comprehension to create a list of the first letters of every word in the string below:

# In[ ]:


st = 'Create a list of the first letters of every word in this string'


# In[12]:


#code here
mystring = "Secret agents are super good at staying hidden."
words = mystring.split()
first_char_list = []
for char in words:
    first_char_list.append(char[0])
print(first_char_list)


# ## GREAT JOB!!

# In[ ]:




