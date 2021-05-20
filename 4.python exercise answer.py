#!/usr/bin/env python
# coding: utf-8

# # Methods and Functions

# ### Write a function that computes the volume of a sphere given its radius

# In[6]:


def vol(radius):
    pi=3.14
    vol=(4.0/3)*pi*(radius**3)
    return vol


# In[7]:


vol(1)


# ### Write a function that checks whether a number is in a given range (Inclusive of high and low)

# In[11]:


def ran_check(num,low,high):
    
    for i in range(low,high+1):
        if num==i:
            print ('Number is within the range')
            break
    else :
            print ('Number is out of range')


# If you only wanted to return a boolean:

# In[13]:


ran_check(4,3,10)


# In[19]:


def ran_bool(num,low,high):
    
    for i in range(low,high+1):
        if num==i:
            print ('True')
            break
    else :
            print ('False')


# In[20]:


ran_bool(3,1,10)


# ### Write a Python function that accepts a string and calculates the number of upper case letters and lower case letters.
# 
# - Sample String : 'Hello Mr. Rogers, how are you this fine Tuesday?'
# #### Expected Output : 
# - No. of Upper case characters : 4
# - No. of Lower case Characters : 33
# 
# HINT: Two string methods that might prove useful: .isupper() and .islower()

# In[23]:


def up_low(s):
    ucount=0
    lcount=0
    for letter in s:
            if str.isupper(letter):
                ucount+=1
            elif str.islower(letter):
                lcount+=1
    print ('count of upper case characters in string is '+str(ucount))
    print ('count of lower case characters in string is '+str(lcount))


# In[24]:


s = 'Hello Mr. Rogers, how are you this fine Tuesday?'
up_low(s)


# ### Write a Python function that takes a list and returns a new list with unique elements of the first list.
# 
# - Sample List : [1,1,1,1,2,2,3,3,3,3,4,5]
# - Unique List : [1, 2, 3, 4, 5]

# In[73]:


def unique_list(l):

    x = []

    for a in l:

        if a not in x:

            x.append(a)

    return x


# In[74]:


unique_list([1,1,1,1,2,2,3,3,3,3,4,5])


# ### Write a Python function to multiply all the numbers in a list.
# 
# - Sample List : [1, 2, 3, -4]
# - Expected Output : -24

# In[37]:


def multiply(numbers):  
      
    product=1
    for num in numbers:
        product=product*num
    return product


# In[38]:


multiply([1,2,3,-4])


# ### Write a Python function that checks whether a word or phrase is palindrome or not.

# In[41]:


def palindrome(s):
    
    reverse_s=s[::-1]
    if s==reverse_s:
        print ('string is palindrome')
    else:
        print ('not a palidrome')


# In[42]:


palindrome('helleh')


# ## GOOD JOB!

# In[ ]:




