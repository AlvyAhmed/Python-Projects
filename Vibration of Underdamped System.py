#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import matplotlib.pyplot as plt
import math 


# In[2]:


A = []

x = np.linspace(0, 4, 150)

for t in x:
    a = 0.647 * (math.exp(-0.92 * t)) - 0.247 * (math.exp(-2.42 * t))
    A.append(a)


# In[3]:


plt.figure(figsize=(10, 3))
plt.ylim(0, 0.5)
plt.plot(x, A)


# In[ ]:




