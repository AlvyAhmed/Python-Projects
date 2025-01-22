#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import matplotlib.pyplot as plt
import math

# stefan boltzman constat

s = 5.67e-8
d1 = 50/1000
d2 = 300/1000
L = 500/1000

A1 = np.pi*d1*L
A2 = np.pi*d2*L

#emissivity

e1 = 0.04
e2 = 0.13

T1 = np.linspace(4,77,30) #k
T2 = 300 #k

q = (s*A1*(T1**4-T2**4))/(((1/e1)+((1-e2)/e2)*(d1/d2)))

print(q)

plt.plot(T1,q)


# In[ ]:




