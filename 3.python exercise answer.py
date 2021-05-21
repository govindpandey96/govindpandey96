#!/usr/bin/env python
# coding: utf-8

# # Function Practice Exercises

# ### LESSER OF TWO EVENS: Write a function that returns the lesser of two given numbers if both numbers are even, but returns the greater if one or both numbers are odd 

#  - lesser_of_two_evens(2,4) --> 2
#  - lesser_of_two_evens(2,5) --> 5

# In[4]:


def lesser_of_two_evens(a,b):
    if a%2 == 0 and b%2 == 0:
        return min(a,b)
    else:
        return max(a,b)


# In[5]:


# Check
lesser_of_two_evens(2,4)


# In[6]:


# Check
lesser_of_two_evens(2,5)


# ### ANIMAL CRACKERS: Write a function that takes a two-word string and returns True if both words begin with same letter
# 
# - animal_crackers('Levelheaded Llama') --> True
# - animal_crackers('Crazy Kangaroo') --> False

# In[7]:


def animal_crackers(words):
    first_word = words.split(" ")[0].lower()
    second_word = words.split(" ")[1].lower()
    if first_word[0] == second_word[0]:
        return True
    else:
        return False


# In[8]:


# Check
animal_crackers('Levelheaded Llama')


# In[9]:


# Check
animal_crackers('Crazy Kangaroo')


# ### OLD MACDONALD: Write a function that capitalizes the first and fourth letters of a name
# 
# old_macdonald('macdonald') --> 'MacDonald'

# In[27]:


def old_macdonald(name):
    if len(name) > 3:
        return name[:3].capitalize() + name[3:].capitalize()
    else:
        return 'Name is too short!'


# In[28]:


# Check
old_macdonald('macdonald')


# ### MASTER YODA: Given a sentence, return a sentence with words reversed
# 
# - master_yoda('I am home') --> 'home am I'
# - master_yoda('We are ready') --> 'ready are We'

# In[15]:


def master_yoda(text):
    return ' '.join(text.split()[::-1])


# In[16]:


# Check
master_yoda('I am home')


# In[17]:


# Check
master_yoda('We are ready') 


# ### ALMOST THERE: Given an integer n, return True if n is within 10 of either 100 or 200
# 
# - almost_there(90) --> True
# - almost_there(104) --> True
# - almost_there(150) --> False
# - almost_there(209) --> True

# In[18]:



def almost_there(n):
    return ((abs(100 - n) <= 10) or (abs(200 - n) <= 10))


# In[20]:


# Check
almost_there(90)


# In[21]:


# Check
almost_there(104)


# In[22]:


# Check
almost_there(150)


# In[23]:


# Check
almost_there(209)


# ### LAUGHTER: Write a function that counts the number of times a given patterns appears in a string, inclusing overlap
# 
# laughter('hah','hahahah') --> 3
# 

# In[9]:


def laughter():

print ("hahahah".count("hah"))


# In[6]:


# Check
laughter('hah','hahahah') 


# ### PAPER DOLL: Given a string, return a string where for every character in the original there are three characters
# 
# - paper_doll('Hello') --> 'HHHeeellllllooo'
# - paper_doll('Mississippi') --> 'MMMiiissssssiiissssssiiippppppiii'

# In[24]:


def paper_doll(text):
    result = ''
    for char in text:
        result += char * 3
    return result


# In[25]:


# Check
paper_doll('Hello')


# In[26]:


# Check
paper_doll('Mississippi')


# ### BLACKJACK: Given three integers between 1 and 11, if their sum is less than or equal to 21, return their sum. If their sum exceeds 21 and there's an eleven, reduce the total sum by 10. Finally, of the sum (even after adjustment) exceeds 21, return 'BUST'
# 
# - blackjack(5,6,7) --> 18
# - blackjack(9,9,9) --> 'BUST'
# - blackjack(9,9,11) --> 19

# In[63]:


def blackjack(x,y,z):
    tot=int(x+y+z)
    if tot < 21:
        return tot
    
    elif tot > 21 and x == 11 or y == 11 or z == 11:
        tot2=tot-10
        return tot2
    
    else:
        return "BUST"
        
    
    


# In[64]:


# Check
blackjack(5,6,7)


# In[65]:


# Check
blackjack(9,9,9)


# In[66]:


# Check
blackjack(9,9,11)


# ### SUMMER OF 69: Return the sum of the numbers in the array, except ignore sections of the numbers starting with a 6 and extending to the next 9(every 6 will be followed by at least one 9). Return 0 for no numbers.
# 
# - summer_69([1, 3, 5]) --> 9
# - summer_69([4,5,6,7,8,9]) --> 9
# - summer_69([2,1,6,9,11]) --> 14

# In[29]:



def summer_69(arr):
    total = 0
    add = True
    for num in arr:
        while add:
            if num != 6:
                total += num
                break
            else:
                add = False
        while not add:
            if num != 9:
                break
            else:
                add = True
                break
    return total


# In[30]:


# Check
summer_69([1, 3, 5])


# In[31]:


# Check
summer_69([4,5,6,7,8,9])


# In[32]:


# Check
summer_69([2,1,6,9,11])


# ## Challenge Problems

# ### SPY GAME: Write a function that takes in a list of integers and returns True if it contains 007 in order
# 
# - spy_game([1,2,4,0,0,7,5]) --> True
# - spy_game([1,0,2,4,0,5,7]) --> True
# - spy_game([1,7,2,0,4,5,0]) --> False

# In[33]:


def spy_game(nums):
 
    code = [0,0,7,'x']
    
    for num in nums:
        if num == code[0]:
            code.pop(0)   # code.remove(num) also works
       
    return len(code) == 1


# In[34]:


# Check
spy_game([1,2,4,0,0,7,5])


# In[35]:


# Check
spy_game([1,0,2,4,0,5,7])


# In[36]:


# Check
spy_game([1,7,2,0,4,5,0])


# ### COUNT PRIMES: Write a function that returns the number of prime numbers that exists up to and including a given number
# 
# count_primes(100) --> 25
# 
# - By convention, 0 and 1 are not prime

# In[37]:


def count_primes(num):
    primes = [2]
    x = 3
    if num < 2:  # for the case of num = 0 or 1
        return 0
    while x <= num:
        for y in range(3,x,2):  # test all odd factors up to x-1
            if x%y == 0:
                x += 2
                break
        else:
            primes.append(x)
            x += 2
    print(primes)
    return len(primes)


# In[38]:


# Check
count_primes(100)


# ## GOOD JOB!!

# In[ ]:




