
import math
import numpy as np


# Code to solve a system of three equations.

# In[5]:


# take in data
n = 3

mat_coeff = [[] for i in range(n)]
const=['a','b','c','d']
print('given the equation ax+by+cz+d')
for i in range(n):
    for j in range(n+1):
        dum = input(f'enter the value of {const[j]}{i+1}: ')
        if dum == None: dum = 0
        mat_coeff[i].append(float(dum))
#     print ('done',mat_coeff)
        


# 
# ## Codes
# ##

# In[32]:


init_guess = [0,0,0]
max_iter =25
tolerance = 10**-16
answers = []
for i in range(n):
    answers.append([init_guess[i],0])
                   


# In[33]:


for _ in range(max_iter):
    
    tolerance_flag = abs(answers[0][0] -answers[0][1]) < tolerance
    
    for i in range(n):
        ans =answers[i]
        res = mat_coeff[i][n]
        for j in range(n):
            if j==i:
                pass
            else:
                res -= mat_coeff[i][j]*answers[j][0]

        ans[1] = res/mat_coeff[i][i]
        tolerance_flag = tolerance_flag and (abs(ans[0]-ans[1]) < tolerance) 
        ans[0]=ans[1]
    if tolerance_flag:break
print(answers,_)


# In[28]:


_


# In[17]:


mat_coeff


# In[20]:


mat_coeff


# In[22]:


b[1]=1


# In[23]:


b


# In[ ]:




