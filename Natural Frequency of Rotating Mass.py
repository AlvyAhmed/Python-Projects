#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import matplotlib.pyplot as plt
import math


# In[2]:


k = 2000 #n*m
m = np.linspace(38,45,10) #kg
x = 0.26 #m

W = []

for y in m:
    w = (k/(y*x**2))**0.5

    W.append(round(w,2))

print(W)


# In[3]:


plt.plot(m,W)


# In[ ]:




