#!/usr/bin/env python
# coding: utf-8

# ## Global Variables:

# + global variables are those variables which are created outside of the functions are known as global variables.
# + global variables are those variables which can be used by everyone, both inside of the function and also outside of the function

# In[2]:


# example; create a variable outside of a function,and use it inside of the function.

x = "Awesome"
def myFunc():
    print("python is " + x)
myFunc()


# ## local variables:

# + if you create a variable with the same name(global variable) inside the function then it is known as local variable.
# + the local variable can be used only inside of the function.
# + the global variable will remain as it is and without change in the original value. 

# In[3]:


# example of local variables:

x = "Awesome"

def MyFunc():
    x = "dynamic language"
    print("python is " + x)

MyFunc()
print("python is " + x)


# ## the Global Keyword:

# + normally, when we create a variable inside a function, that variable is local and can only be used inside that function.
# + to create a global variable inside a function,you can use the "global" keyword.
# + if we use the global keyword the scope of the local variable converts into global.

# In[4]:


# example of global keyword:

x = "awesome"

def my_func():
    
    global x
    x = "dynamic language"
    print("python is " + x)
my_func()
print("python is " + x)


# In[ ]:




