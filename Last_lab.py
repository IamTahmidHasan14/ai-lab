
# coding: utf-8

# In[19]:

#lab_quiz: overfitting, underfitting, crossvalidation, confusionmatrix, bias_varience, ---> seabon

#sklearn,seaborn theke onno dataset niye lab report

from sklearn import datasets
a=datasets.load_iris()
#dir(a)
#print(a.DESCR)
print(a.feature_names)
#print(a.target)


# In[38]:

get_ipython().magic('matplotlib inline')
import seaborn as sns
data=sns.load_dataset('iris')
relation=data.corr()
print(relation)
sns.heatmap(relation,cmap='coolwarm',annot=True)


# In[2]:

pip install pycaret
from pycaret.datasets import get_data
#a=get_data('index')
a=get_data('iris')
from pycaret.classification import *
exp=setup................


# In[4]:

import sys
print("User Current Version:-", sys.version)


# In[ ]:



