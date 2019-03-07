
# coding: utf-8

# In[1]:


#Advantages of usning numpy's universal function
import numpy as np


# In[26]:


#Without using numpy the speed of the loop is 90microsec
list1 = list(range(1000))
get_ipython().magic('timeit newlist = [i + 2 for i in list1]')


# In[27]:


#Now converting the list into numpy
#The same loop now takes 3 microsec
arr1 = np.array(list1)
get_ipython().magic('timeit newlist = arr1 + 2')


# In[4]:


#Advantages of Using numpy's aggreagations


# In[23]:


#Making a list of 10000 random numbers
from random import random
list2 = [random() for i in range(10000)]


# In[24]:


#Calculating the minimum of the list
get_ipython().magic('timeit min(list2)')


# In[25]:


#Now converting list2 to numpy2 array
numpy2 = np.array(list2)
get_ipython().magic('timeit numpy2.min()')


# In[30]:


#Usage in multidimensional arrays
numpy3 = np.random.randint(0,10,(3,5))
numpy3


# In[36]:


numpy3.mean()


# In[43]:


numpy3.argmax(axis=1)


# In[35]:


#Printing the sum column wise and row wise
numpy3.sum(axis=0) 


# In[34]:


numpy3.sum(axis=1)


# In[44]:


#Numpy for broadcasting
#Broadcasting is stretching one matrix to equal to the dimension of the other matrix
#The general matrix functionality applies in broadcasting - when a 3*1 matrix is added to 1*3 matrix a 3*3 matrix is formed
np.ones(3) + 5


# In[47]:


np.arange(3).reshape(3,1) + np.arange(3)


# In[ ]:


#Using numpy's slicing, masking, and fancy indexing


# In[48]:


#Using masking in indexing
numpyar = np.array(range(6))


# In[51]:


mask = [True, False, True, False, False, True]


# In[52]:


numpyar[mask]


# In[62]:


mask = (numpyar>3) & (numpyar<5)
mask


# In[63]:


numpyar[mask]


# In[64]:


#Using fancy indexing
ind = [1,3,4]


# In[65]:


numpyar[ind]


# In[66]:


#Using masking and slice in a multidimensional array
narray = np.arange(3).reshape(3,1) + np.arange(3)


# In[74]:


narray[narray.sum(axis = 1) > 4, :2]

