#!/usr/bin/env python
# coding: utf-8

# In[7]:


import numpy
import numpy as np
import matplotlib.pyplot as plt
import math

h=50
h1=h/2
a1= math.sqrt(3)/2
x= np.array([0,h1-a1*h1,h1/2,h1,h1+(h1/2),a1*h1+h1,h])
theta1= np.linspace(0,120,7)
theta2= np.linspace(180,270,7)

X = np.flip(x)

fig = plt.subplots(figsize=(20,8))
plt.grid(True)
plt.xlabel('Theta')
plt.ylabel('Lift')
plt.xticks(np.arange(0,280,step=10))
plt.yticks(np.arange(0,55,step=2))
plt.plot(theta1,x,theta2,X)


# In[ ]:




