
import matplotlib.pyplot as plt

import math

def my_solve(a,init_guess= [0.1,3]):
    total_ans =[]
    ans = init_guess[0]
    for i in range(15):
        ans =(ans**2 *math.cos(ans)-a)/(math.sin(ans)+ans*math.cos(ans))
    total_ans.append(round(ans,2))
    ans = init_guess[1]
    for i in range(15):
        ans =(ans**2 *math.cos(ans)-a)/(math.sin(ans)+ans*math.cos(ans))
    total_ans.append(round(ans,2))
    return total_ans

print(my_solve(0))


# In[30]:


## loop a values from-0.2 to 0.2 in steps of 0.025
###
n = int((0.2--0.2)/0.025)
a_values = []
sol_values =[]

for i in range(n+1):
    a = round(-0.2 +i*0.025,3)
    sol = my_solve(a)
    sol_values.extend(sol)
    a_values.extend([a]*len(sol))
print(a_values)
print(sol_values)


def clean_result(sol,a):
    sol = sol.copy()
    a = a.copy()
    ele =[]
    for i in range(len(sol)):
        if abs(sol[i] ) > math.pi:
            ele.append(i)
    for i in range(len(ele)):
        p = len(ele) - i-1
        sol.pop(ele[p])
        a.pop(ele[p])
    return sol,a
sol_values,a_values = clean_result(sol_values,a_values)


# In[41]:


print(sol_values)
print(a_values)


# In[42]:


plt.plot(a_values,sol_values)

plt.show()
# In[15]:


print(a_values)
print(sol_values)




