#!/usr/bin/env python
# coding: utf-8

# In[8]:


import numpy as np
import matplotlib.pyplot as plt
import sympy as sp
import math

sp.init_printing(use_latex="mathjax")
r1 = 0.2 #m radius
r = sp.symbols("r")
v=(3*(1-25*r**2))
display(v)

da=2*3.14*r
vda=v*da
display(vda)

Q=sp.integrate(vda,(r,0,r1))

print( "Volumetric flow is",round(Q,4), "m3/s")

V = Q/(3.14*r1**2)

print("average velocity is",round(V,4),"m2/s")


# In[ ]:




