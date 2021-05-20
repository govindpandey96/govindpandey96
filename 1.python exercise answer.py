#!/usr/bin/env python
# coding: utf-8

# # NUMBERS

# ### Write an equation using multiplication, division , an exponent, addition and substraction that is equal to 125.26

# In[48]:


10*10/1+6**2-10.74


# ### Answer these three questions without typing code. then type code to check your answer 
# 
# - What is the value of expression 4 * (6 + 5)
# - What is the value of expression 4 * 6 + 5
# - What is the value of expression 4 + 6 * 5

# In[23]:


4*(6+5)


# In[24]:


4*6+5


# In[25]:


4+6*5


# ### What is the type of the result of the expression 3 + 1.5 + 4?

# In[26]:


3+1.5+4


# ### What would you use to find the nnumber's square root, as well as square?

# In[50]:


print(3**2)  #squared (raise to the power of 2)


# In[49]:


print(3**0.5)  #squars root (raise to the power of 1/2)


# # STRINGS

# ### Given the string 'hello' give an index command that returns 'e'. Enter your code in the cell below.

# In[33]:


s = 'hello'
# Print out 'e' using indexing
# code here 
s[1]


# ### Reverse the string 'hello' using slicing

# In[35]:


s = 'hello'
# Reverse the string using slicing
print(s[::-1])
#code here


# ### Given the string hello, give two methods of producing the letter 'o' using indexing.

# In[37]:


s = 'hello'
# Print out the 'o'
#code here 
print(s[-1])


# In[38]:


print(s[4])


# # LISTS

# ### Build this list [0,0,0] in two separate ways

# In[40]:


l = [0,0,0]
print (l)
l = [0]*3
print(l)


# In[42]:


l1 = list()
l1.append(0)
l1.append(0)
l1.append(0)
print(l1)
l1 = [0]*3
print(l1)


# ### Reassign 'hello' in this nested list to say 'goodbye' instead

# In[44]:


l = [1,2,[3,4,'hello']]
l1 =l[2]
l1[l1.index('hello')] = 'goodbye'
print(l)


# ### Sort the list bellow:

# In[45]:


l = [5,3,4,6,1]
l.sort()
print(l)
l = [5,3,4,6,1]
print(sorted(l))


# # DICTIONARIES

# ### Using keys and indexing, grab the 'hello' from the following dictionaries:

# In[11]:


d = {'simple_key':'hello'}
# Grab 'hello'
print(d['simple_key'])


# In[12]:


d = {'k1':{'k2':'hello'}}
# Grab 'hello'
print(d['k1']['k2'])


# In[15]:


d = {'k1':[{'nest_key':['this is deep',['hello']]}]}
# Grab 'hello'
print(d['k1'][0]['nest_key'][1][0])


# In[16]:


d = {'k1':[1,2,{'k2':['this is tricky',{'tough':[1,2,['hello']]}]}]}
# Grab 'hello'
print(d['k1'][2]['k2'][1]['tough'][2][0])


# ### Can you sort a dictionary? Why or why not?

# In[ ]:


Because it is keys and values.


# # TUPLES

# ### What is the major difference between tuples and lists?

# In[ ]:


Tuples are immutable and lists are mutable.


# ### How do you create a tuple?

# In[ ]:


with parentheses and a comma delimited list (5,2.1)


# # SETS

# ### Use a set to find the unique values of the list bellow:

# In[8]:


list3 = [1,2,2,33,4,4,11,22,3,3,2]


# In[18]:


l = [1,2,2,33,4,4,11,22,3,3,2]
print (l)
s = set(l)
print(s)


# # BOOLEANS

# ### What will be the resulting Boolean of the following pieces of code (answer first them check by typing it in!)

# In[2]:


3 <= 2


# In[1]:


2 > 3


# In[3]:


3 == 2.0


# In[4]:


3.0 == 3


# In[5]:


4**0.5 != 2


# ### What is the boolean output of the cell block below?

# In[22]:


#  two nested lists
l_one = [1,2,[3,4]]
l_two = [1,2,{'k1':4}]

# True or False?
#3>=4
#False
l_one[2][0] >= l_two[2]['k1']


# ## GOOD JOB!!

# 
