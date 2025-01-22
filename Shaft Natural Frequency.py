#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import math as m


# In[2]:


p = 10 #kg
l = 500 #mm
E = 2.1e5 #MPa
d = 30 #mm

I = ((m.pi)/64)*(d**4)

P = p*9.81
delta = (P*l**3)/(3*E*I)


# In[3]:


print("The delta of the system is:", delta)


# In[4]:


wn = m.sqrt(9.81/delta)

print("The omega of the system is:", wn)


# In[5]:


fn = wn/(2*(m.pi))

print("natural frequency of the system is:", fn)


# In[ ]:




