#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import matplotlib.pyplot as plt
import math


# In[4]:


A = []

x = np.linspace(0, 20, 1000)

for t in x:
    a = (math.exp(-.3742*t))*((0.06*math.cos(6.577*t)) + (0.1859*math.sin(6.577*t)))
    A.append(a)


# In[5]:


plt.figure(figsize=(10, 5))
plt.ylim(-0.2, 0.2)
b = ([0,20])
B = ([0,0])
plt.plot(x, A, b, B)


# In[ ]:




