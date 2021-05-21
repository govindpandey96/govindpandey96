#!/usr/bin/env python
# coding: utf-8

# # Generators

# ### Create a generator that generates the squares of numbers up to some number N.

# In[1]:


def gensquares(N):

    for i in range(N): 
        yield i**2


# In[2]:


for x in gensquares(10):
    print(x)


# ### Create a generator that yields "n" random numbers between a low and high number (that are inputs).
# Note: Use the random library.

# In[34]:


import random

random.randint(1,10)


# In[43]:


def rand_num(low,high,n):
  for i in range(n+1):
        yield random.randint(low, high)


# In[44]:


for num in rand_num(1,10,12):
    print(num)


# ### Use the iter() function to convert the string below into an iterator:

# In[49]:


s = 'hello'

#code here
for letter in iter(s):
    print (letter)


# In[ ]:




