#!/usr/bin/env python
# coding: utf-8

# In[16]:


import numpy as np
from sympy.solvers.solveset import nonlinsolve
from sympy import Symbol
from sympy import *
import math
import csv


# In[51]:


R = Matrix()

#Read rijxcolumnes file
with open('rijxcolumnes') as file:
    csv_reader = csv.reader(file, delimiter=',')
    for r in csv_reader:
        R = Matrix([[r[0], r[3], r[6]],
                    [r[1], r[4], r[7]],
                    [r[2], r[5], r[8]]])
R


# In[ ]:


# gamma -> fi_x
# beta -> fi_y
# alpha -> fi_z

gamma = Symbol('gamma')
beta = Symbol('beta')
alpha = Symbol('alpha')

eq_beta = -sin(beta) - R[2,0]
fi_y = solve(eq_beta, beta)[0]
fi_y

eq_alpha = cos(fi_y)*cos(alpha) - R[0,0]
fi_z = solve(eq_alpha, alpha)[0]
fi_z

eq_gamma = cos(fi_y)*sin(gamma) - R[2,1]
fi_x = solve(eq_gamma, gamma)[0]
fi_x

print(math.degrees(fi_x), math.degrees(fi_y), math.degrees(fi_z))


# In[58]:


with open('fisef.out', 'w') as file:
    writer = csv.writer(file, delimiter=',')
    writer.writerow([round(math.degrees(fi_z), 2), round(math.degrees(fi_y), 2), round(math.degrees(fi_x), 2)])

