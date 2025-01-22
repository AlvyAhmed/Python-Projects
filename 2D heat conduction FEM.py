#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
import matplotlib.pyplot as plt

maxIter=500

lenX=10
lenY=10

delta=1

Ttop=500
Tbottom=30
Tleft=30
Tright=30

Tinitial=30

colorinterpolation=50
colormap=plt.cm.jet

X,Y = np.meshgrid(np.arange(0,lenX),np.arange(0,lenY))

T = np.empty((lenX,lenY))
T.fill(Tinitial)

#Boundary conditions

T[(lenY-1):,:]=Ttop
T[:1,:]=Tbottom
T[:,(lenX-1):]=Tright
T[:,:1]=Tleft

print(T[(lenY-1):,:],T[:1,:],T[:,(lenX-1):],T[:,:1])

print("please wait for some time while solving equation")

for iteration in range(0,maxIter):
    for i in range(1,lenX-1,delta):
        for j in range(1,lenY-1,delta):
            T[i,j]=0.25*(T[i+1][j]+T[i-1][j]+T[i][j+1]+T[i][j-1])

print("iteration is over")

plt.title("Contour of temperature of 2D plot")
plt.contourf(X,Y,T, colorinterpolation, cmap=colormap)
plt.colorbar()
plt.show()


# In[ ]:





# In[ ]:




