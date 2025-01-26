#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
import matplotlib.cm as cm
import matplotlib.pyplot as plt
import matplotlib

p=20
ro=1500
ri=1490

x=np.linspace(ro,ri,100)
stress=((p*ri**2)/(ro**2-ri**2))*((x**2-ro**2)/x**2)
plt.plot(x,stress)

X,Y=np.meshgrid(x,stress)
Z=(X)

fig,ax=plt.subplots(1,1)
cp=ax.contourf(X,Y,Z)
fig.colorbar(cp)
ax.set_title("Stress Across Thickness")
ax.set_xlabel("Radius (mm)")
ax.set_ylabel("Stress (MPa)")
plt.style.use('classic')
plt.show()


# In[ ]:




