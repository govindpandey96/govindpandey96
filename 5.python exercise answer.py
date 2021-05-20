#!/usr/bin/env python
# coding: utf-8

# # Object Oriented Programming

# ### Fill in the Line class methods to accept coordinates as a pair of tuples and return the slope and distance of the line.

# In[5]:


class Line:
    
    def __init__(self,coor1,coor2):
        self.coor1 = coor1
        self.coor2 = coor2
    
    def distance(self):
        return ((self.coor2[0] - self.coor1[0])**2 +                 (self.coor2[1] - self.coor1[1])**2)**0.5
    
    def slope(self):
        return (self.coor2[1] - self.coor1[1]) /                 (self.coor2[0] - self.coor1[0])


# In[6]:


# EXAMPLE OUTPUT

coordinate1 = (3,2)
coordinate2 = (8,10)

li = Line(coordinate1,coordinate2)


# In[7]:


li.distance()


# In[8]:


li.slope()


# ### Fill in the class

# In[11]:


class Cylinder(object):
    pi = 3.14
    
    def __init__(self,height=1,radius=1):
        self.height = height
        self.radius = radius
        
    def volume(self):
        return Cylinder.pi * (self.radius**2) * self.height
    
    def surface_area(self):
        circles = 2 * Cylinder.pi * self.radius**2
        wall = 2 * Cylinder.pi * self.radius * self.height
        return circles + wall


# In[12]:


# EXAMPLE OUTPUT
c = Cylinder(2,3)


# In[13]:


c.volume()


# In[14]:


c.surface_area()


# ## Challenge Problem

# For this challenge, create a bank account class that has two attributes:
# 
# - owner
# - balance
# 
# and two methods:
# 
# - deposit
# - withdraw
# 
# As an added requirement, withdrawals may not exceed the available balance.
# 
# Instantiate your class, make several deposits and withdrawals, and test to make sure the account can't be overdrawn.

# In[15]:


class Account:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance
        
        
    def __str__(self):
        return('Account owner: {} \nAccount balance {}'.format(self.owner, self.balance))
        
    def deposit(self, deposit_amt):
        
        self.balance = self.balance + deposit_amt
        print('You have been credited with {} and your current balance is {}'.format(deposit_amt, self.balance))
        
    def withdraw(self, withdraw_amt):
         
            if withdraw_amt > self.balance:
                print('Funds Unavailable, You have only {} in your account'.format(self.balance))
            else:
                self.balance = self.balance - withdraw_amt
                print('Withdrawal Accepted and your current balance is {}'.format(self.balance))
        
    


# In[16]:


# 1. Instantiate the class
acct1 = Account('Jose',100)


# In[17]:


# 2. Print the object
print(acct1)

# Output- Account owner:   Jose
#         Account balance: $100


# In[18]:


# 3. Show the account owner attribute
acct1.owner


# In[19]:


# 4. Show the account balance attribute
acct1.balance


# In[20]:


# 5. Make a series of deposits and withdrawals
acct1.deposit(50)

#Output - Deposit accepted


# In[21]:


acct1.withdraw(75)

#Output - Withdrawal accepted


# In[22]:


# 6. Make a withdrawal that exceeds the available balance
acct1.withdraw(500)

#Output - Funds Unavailable


# ## GOOD JOB!!

# In[ ]:




