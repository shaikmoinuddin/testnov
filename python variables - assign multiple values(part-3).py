#!/usr/bin/env python
# coding: utf-8

# ### Many values to multiple variables:

# + python allows you to assign values to multiple variables in one line
# + make sure the number of values should be equal to the number of variables or else we gat an error.

# In[1]:


# example:

x, y, z = "apple","ball","cat"
print(x)
print(y)
print(z)


# In[2]:


# example of values are not equal to the variables.

x, y, z = "dog","eagle"
print(x)
print(y)


# ### One value Multiple variables:

# + we can assign same value to multiple variables

# In[3]:


# example:

x = y = z = "fish"
print(x)
print(y)
print(z)


# ### Unpack a Collection:

# + if we have a collection of values like list or tuple etc, python allows you to extract the values into variables.this is called unpacking

# In[5]:


# example of unpacking:

fruits = ["apple","banana","mango","watermelon","pineapple"]
a,b,c,d,e = fruits
print(a)
print(b)
print(c)
print(d)
print(e)


# In[ ]:




