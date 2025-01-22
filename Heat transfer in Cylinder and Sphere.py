#!/usr/bin/env python
# coding: utf-8

# In[3]:


import numpy as np
import matplotlib.pyplot as plt
import math

Q = int(input("For cylinder press 1, For Spherical press 2:"))
Tin = float(input("Temperature at inner radius (K):"))
Tout = float(input("Temperature at outer radius (K):"))
r1 = float(input("inner radius (mm):"))
t = float(input("thickness (mm):"))

#program begins

r2 = r1 + t
R = np.linspace(r1,r2,50)

if Q == 1:
    T = Tin+((Tout-Tin)*(np.log(R/r1))/math.log(r2/r1))
elif Q == 2:
    T = Tin+((Tout-Tin)*((1/r1)-(1/R))/((1/r1)-(1/r2)))

plt.plot(R,T)
X,Y = np.meshgrid(R,T)
Z = (X)

fig,ax=plt.subplots(1,1)
cp=ax.contourf(X,Y,Z)
fig.colorbar(cp)
ax.set_title("Temperature along radius")
ax.set_xlabel("Radius (mm)")
ax.set_ylabel("Temperature")
plt.style.use('classic')
plt.show()


# In[ ]:




