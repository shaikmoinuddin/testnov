#!/usr/bin/env python
# coding: utf-8

# ### Output Variables:

# + the python print() function is often used to output variables.
# + in the print() function,we can output multiple variables, seperated by a comma(,)
# + we can also use "+" operator to output multiple variables.
# + Notice the space character after "Python " and "is ", without them the result would be "Pythonisawesome".
# + for numbers "+" works as a mathematical operator.

# In[1]:


# example:

x = "python is awesome"
print(x)


# In[2]:


# example:in the print() function,we can output multiple variables, seperated by a comma(,)

x = "python"
y = "is"
z = "awesome"
print(x,y,z)


# In[3]:


# example: we can also use "+" operator to output multiple variables.

a = "python"
b = "is"
c = "awesome"
print(a + b + c)


# In[4]:


# example: Notice the space character after "Python " and "is ", without them the result would be "Pythonisawesome".

a = "python "
b = "is "
c = "awesome "
print(a+b+c)


# ## In the print() function, when you try to combine a string and a number with the "+" operator , python will give you an error. 

# In[5]:


# example:

x = "python"
y = 3
print(x+y)


# ## the best way to output multiple variables in the print() function is to seperate them with commas, which even support different datatypes.

# In[6]:


# example:

x = "python"
y = 3
print(x,y)


# In[ ]:




