
# coding: utf-8

# In[1]:

dataset={
    'k':[[208,136],[196,119],[184,114]], #wrestler
    'r':[[170,67],[185,81]] #footballer
}
#print(dataset)


# In[4]:

import matplotlib.pyplot as plt
from matplotlib import style
style.use('fivethirtyeight')

for i in dataset:
    for j in dataset[i]:
        plt.scatter(j[0],j[1],color=i)
plt.show()


# In[ ]:

while True:
    new_one=input('Enter new sample [height,weight]:').split(',')
    new_sample=[]
    new_sample.append(int(new_one[0]))
    new_sample.append(int(new_one[1]))
    if new_sample==[0,0]:
        break
    else:
        print(new_sample)


# In[ ]:

a=int(input('Enter a number: '))
b=int(input('Enter another number: '))
c=a+b
print(c)

