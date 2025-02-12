#!/usr/bin/env python
# coding: utf-8

# In[5]:


from pulp import *

#Minimization problem
prob = LpProblem("Mininizationoftrasportationcost",LpMinimize)

#variable define
x1=LpVariable("x1", lowBound=0, cat='Integer')
x2=LpVariable("x2", lowBound=0, cat='Integer')
x3=LpVariable("x3", lowBound=0, cat='Integer')
x4=LpVariable("x4", lowBound=0, cat='Integer')
x5=LpVariable("x5", lowBound=0, cat='Integer')
x6=LpVariable("x6", lowBound=0, cat='Integer')

#objective Function
prob += 14*x1+13*x2+11*x3+13*x4+13*x5+12*x6

#constrain
prob += x1+x2+x3<=1200
prob += x4+x5+x6<=1000
prob += x1+x4>=1000
prob += x2+x5>=700
prob += x3+x6>=500
prob

#solve
status = prob.solve()
LpStatus[status]

#print
print("Objective value is :", value(prob.objective))
print("X1 value is :", value(x1))
print("X2 value is :", value(x2))
print("X3 value is :", value(x3))
print("X4 value is :", value(x4))
print("X5 value is :", value(x5))
print("X6 value is :", value(x6))


# In[ ]:




