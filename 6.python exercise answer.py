#!/usr/bin/env python
# coding: utf-8

# # Errors and Exceptions

# ### Handle the exception thrown by the code below by using try and except blocks.

# In[1]:


for i in ['a','b','c']:
    try: 
        print (i**2)
    except:
        print ("Not an integer")


# ### Handle the exception thrown by the code below by using try and except blocks. Then use a finally block to print 'All Done.'

# In[3]:


x = 5
y = 0
try: 
    z = x/y
except:
    print ("x/y Division could not be performed")
finally:
    print ("All done!")


# ### Write a function that asks for an integer and prints the square of it. Use a while loop with a try,except, else block to account for incorrect inputs. 

# In[ ]:


def ask():
    
    while True:
        try:
            n = input('Input an integer: ')
        except:
            print ('An error occurred! Please try again!')
          continue
        else:
            break
            
        
    print ('Thank you, you number squared is: ',n**2)


# In[ ]:


ask()


#     Output:
#     Input an integer: null
#     An error occurred! Please try again!
#     Input an integer: 2
#     Thank you, your number squared is:  4

# ## GOOD JOB!

# In[ ]:




