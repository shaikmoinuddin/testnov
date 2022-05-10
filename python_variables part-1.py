#!/usr/bin/env python
# coding: utf-8

# ### python variables:

# + variables are containers for storing the data values.

# ### creating variables:

#  + python has no command for declaring a variable
#  + a variable is created the moment you first assign a value to it.
#  + variables do not need to be declared to be particular type,and even can change type after they have been set.
#  + variables are case-sensitive.

# ### example:

# In[1]:


x = 5
y = "John"
print(x)
print(y)


# ### casting

# + if we want to specify the data type of a variable,this can be done with casting.

# In[ ]:


# example:

x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0


# ### get the type:

# + we can get the type of the data using type() function.

# In[2]:


# example:

x = 5
y = "John"
print(type(x))
print(type(y))


# ### single quotes or double quotes?

# + string variables can be declared by using either single quotes or double quotes.

# In[ ]:


# example:

x = "John"
# is the same as
x = 'John'b


# ### case-sensitive:

# + variable names are case-sensitive.

# In[ ]:


# example:

a = 4
A = "Sally"
#A will not overwrite a

