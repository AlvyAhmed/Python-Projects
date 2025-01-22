#!/usr/bin/env python
# coding: utf-8

# In[4]:


import cmath
import numpy
import matplotlib.pyplot as plt

cnum = 1.6 + 1.5j
print("Absolute value of 4-5j is:", abs(cnum))

phase = cmath.phase(cnum)
print("phase in degrees =", numpy.degrees(phase))

x = numpy.linspace(0,100,200)
y = 1.875*numpy.log(x/2)+3


plt.title("velocity of bubble")
plt.xlabel("length in meters")
plt.ylabel("length in meters")
plt.plot(x,y)


# In[ ]:




