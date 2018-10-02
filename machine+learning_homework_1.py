
# coding: utf-8

# In[15]:

# add this line if you want to run the code in python2 !!
from __future__ import division,print_function

import numpy as np
import matplotlib.pyplot as plt
import scipy.io
import math

#add this line if you run any code containing plot in jupyter notebook - Remember!
get_ipython().magic(u'matplotlib inline')


# In[16]:

# Q1
# Minors - Exponential
# Teens - Exponential
# Adults - Exponential


# In[17]:

# Q2 第一列为classnum的所有行的第二列的mean
def learnLambda(data, class_num):
    return 1 / data[np.where(data[:,0]==class_num)][:,1].mean()


# In[18]:

# Q3
def labelML(amount_alc, lambdas):
    y_m = lambdas[0] * math.exp(-lambdas[0] * amount_alc)
    y_t = lambdas[1] * math.exp(-lambdas[1] * amount_alc)
    y_a = lambdas[2] * math.exp(-lambdas[2] * amount_alc)
    if y_m > y_t and y_m > y_a:
        return 'M'
    elif y_t > y_a:
        return 'T'
    else:
        return 'A'


# In[19]:

# Q4
def learnPrior(data, class_num):
    num = len(np.where(data[:,0] == class_num))
    return num / len(df)


# In[20]:

# Q5
def evaluateML(test_data, lambdas):
    cnt = 0
    correctLabel = {"M":1, "T":2, "A":3}
    for i in range(len(test_data)):
        data = test_data[i]
        if correctLabel[labelML(data[1], lambdas)] == data[0]:
            cnt  += 1
    return cnt / len(test_data)


# In[21]:

# Q6
# 6 samples correct rate: 0.38666666666666666
# 54 samples correct rate: 0.5833333333333334
# 162 samples correct rate: 0.5833333333333334

data = scipy.io.loadmat('/Users/annettechiu/Downloads/hw1data.mat')
train = data["trainData"]
test = data["testData"]

#选出train这个matrix中第一列为1的行

minors = train[np.where(train[:,0] == 1)]
plt.title("Minors")
plt.hist(minors[:,1])
plt.show()

teens = train[np.where(train[:,0] == 2)]
plt.title("Teens")
plt.hist(teens[:,1])
plt.show()

adults = train[np.where(train[:,0] == 3)]
plt.title("Adults")
plt.hist(adults[:,1])
plt.show()


lambdas = []
for i in range(3):
    lambdas.append(learnLambda(data["trainData"][:6,:], i + 1))

print("6 samples correct rate:", evaluateML(test, lambdas ))

lambdas = []
for i in range(0,3):
    lambdas.append(learnLambda(data["trainData"][:54,:], i + 1))

print("54 samples correct rate:", evaluateML(test, lambdas ))


lambdas = []
for i in range(0,3):
    lambdas.append(learnLambda(data["trainData"][:162,:], i + 1))
print("162 samples correct rate:", evaluateML(test, lambdas ))


# In[ ]:




# In[ ]:




# In[ ]:



