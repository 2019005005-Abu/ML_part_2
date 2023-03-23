#!/usr/bin/env python
# coding: utf-8

# In[16]:


import pandas as pd
Age=pd.Series([10,20,30,40],index=["ag1","ag2","ag3","ag4"]);
print(Age);


# In[17]:



FilterAge=Age[Age>10]
print(FilterAge)


# In[9]:


(/values)
print(Age.values)


# In[10]:


(/index)
print(Age.index)


# In[14]:



AgeIndex=Age.index=['A1','A2','A3','A4'];
print(AgeIndex)


# In[24]:


import numpy as np;
DF=np.array([[20,10,8],[25,8,10],[27,5,3],[30,9,7]]);
DataSet=pd.DataFrame(DF);
print(DataSet);
print("\n");
convertingnp=np.array(DataSet)
print(convertingnp)
Data_set=pd.DataFrame(DF,index=['s1','s2','s3','s4'])
print(Data_set);
Data_set2=pd.DataFrame(DF,index=['s1','s2','s3','s4'],
columns=['Age','Grade1','Grade2']);
print(Data_set2)
Data_set2['Grade3']=[9,6,7,10];
print(Data_set2)


# In[30]:


print(Data_set2).loc['s2']
print(Data_set2.loc[1][3])


# In[31]:


print(Data_set2.iloc[1][3])


# In[32]:


print(Data_set2.iloc[:,0])


# In[33]:


print(Data_set2.iloc[:,3]);


# In[35]:


print(Data_set2.iloc[:,2]);


# In[36]:


Filter_Data=Data_set2.iloc[:,1:2];
print(Filter_Data)


# In[ ]:




