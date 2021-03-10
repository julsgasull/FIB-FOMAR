#!/usr/bin/env python
# coding: utf-8

# # Building the complete rotation matrix from my ID number: [49244309]

# In[29]:


import numpy as np
from sympy.solvers.solveset import nonlinsolve
from sympy import Symbol
from sympy import *
import math


# #### Assigning value to 3 elements of the matrix based on my ID number

# In[11]:


x1 = 0.90
x3 = 0.34
z1 = 0.42


# #### Finding out x2 and y1 elements using the unit vector property of rotation matrices

# In[15]:


x2 = np.sqrt(1 - x1**2 - x3**2)
y1 = np.sqrt(1 - z1**2 - x1**2)
print(f'x2 = {x2}\ny1 = {y1}')


# #### Finding out the remaining values using the orthonormality and unit vector properties

# In[56]:


y2 = Symbol('y_2')
y3 = Symbol('y_3')
z2 = Symbol('z_2')
z3 = Symbol('z_3')

#Defining the R matrix we want to find out


#Find y2 and y3. 
c1_c2_eq = x1*y1 + x2*y2 + x3*y3
c2_c2_eq = y1*y1 + y2*y2 + y3*y3 - 1

#Two solutions were provided. The first one is chosen
y2, y3 = nonlinsolve([c1_c2_eq, c2_c2_eq] , [y2, y3]).args[0]


#Find z2 and z3
c1_c3_eq = x1*z1 + x2*z2 + x3*z3
c2_c3_eq = y1*z1 + y2*z2 + y3*z3
c3_c3_eq = z1*z1 + z2*z2 + z3*z3 - 1

z2, z3 = nonlinsolve([c1_c3_eq, c2_c3_eq, c3_c3_eq] , [z2, z3]).args[0]

R = Matrix([[x1, y1, z1],
            [x2, y2, z2],
            [x3, y3, z3]])


# #### So, the R matrix is as follows

# In[57]:


R


# -------------------------------------------------------------------------------------------------

# In[58]:


fi_x = Symbol('fi_x')
fi_y = Symbol('fi_y')
fi_z = Symbol('fi_z')

R = Matrix([[0.5363, 0.6830, -0.4958], 
            [-0.3020, 0.7039, 0.6429], 
            [0.7881, -0.1951, 0.5838]]
          ).transpose()
R


# In[59]:


R = Matrix([[0.5363, 0.6830, -0.4958], 
            [-0.3020, 0.7039, 0.6429], 
            [0.7881, -0.1951, 0.5838]]
          ).transpose()
R


# In[60]:


Rz = Matrix([[cos(fi_z), -sin(fi_z), 0],
             [sin(fi_z), cos(fi_z), 0], 
             [0,0,1]])
Ry = Matrix([[cos(fi_y), 0, sin(fi_y)],
             [0, 1, 0],
             [-sin(fi_y), 0, cos(fi_y)]])
Rx = Matrix([[1,0,0],
             [0, cos(fi_x), -sin(fi_x)],
             [0, sin(fi_x), cos(fi_x)]])

R_fin = Rz*Ry*Rx


# In[61]:


equations_system = (R_fin[0,2] - R[0,2],
                    R_fin[2,1] - R[2,1],
                    R_fin[1,0] - R[1,0])


# **Get the solutions to the equations system**

# In[62]:


solutions_rad = solve(equations_system, fi_z, fi_y, fi_x)


# **Angles are in radians. Convert them to degrees**

# In[38]:


solutions_deg = []
for i in solutions:
    solutions_deg.append(tuple((math.degrees(i[0]), math.degrees(i[1]), math.degrees(i[2]))))
    print(math.degrees(i[0]), math.degrees(i[1]), math.degrees(i[2]))


# **4th solution from "solutions" is the right one**

# In[40]:


solutions_deg[4]

