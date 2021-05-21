#!/usr/bin/env python
# coding: utf-8

# # Advanced Python Objects and Data Structures

# ## Advanced Numbers
# #### Convert 1024 to binary and hexadecimal representation

# In[3]:


print (bin(1024))


# In[4]:


print (hex(1024))


# #### Round 5.23222 to two decimal places

# In[5]:


print (round(5.2322, 2))


# ## Advanced Strings

# #### Check if every letter in the string s is lower case

# In[9]:



s = 'hello how are you Mary, are you feeling okay?'
print ('Yup' if s.islower() else 'Nope')


# #### How many times does the letter 'w' show up in the string below?

# In[10]:


s = 'twywywtwywbwhsjhwuwshshwuwwwjdjdid'
print (s.count('w'))


# ## Advanced Sets

# #### Find the elements in set1 that are not in set2

# In[13]:


set1 = {2,3,1,5,6,8}
set2 = {3,1,7,5,6,8}
print (set1.difference(set2)) 
print (set2.difference(set1)) 


# #### Find all elements that are in either set

# In[14]:


print (set1.union(set2)) 
print (set1.intersection(set2)) 


# ## Advanced Dictionaries

# #### Create this dictionary: {0: 0, 1: 1, 2: 8, 3: 27, 4: 64} using a dictionary comprehension.

# In[15]:


{x:x**3 for x in range(5)}


# ## Advanced Lists

# #### Reverse the list below

# In[20]:


list1 = [1,2,3,4]
list1.reverse() 
list1


# #### Sort the list below in reverse order

# In[21]:


list2 = [3,4,2,5,1]
list2.sort()
list2


# ## Great Job!
