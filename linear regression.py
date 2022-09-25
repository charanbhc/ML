#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
from sklearn import linear_model
import matplotlib.pyplot as plt


# In[3]:


df=pd.read_csv("https://raw.githubusercontent.com/charanbhc/py/master/ML/1_linear_reg/homeprices.csv")


# In[4]:


get_ipython().run_line_magic('matplotlib', 'inline')
plt.xlabel('area')
plt.ylabel('price')
plt.scatter(df.area,df.price,color='red',marker='+')


# In[5]:


new_df = df.drop('price',axis='columns')
new_df


# In[6]:


price = df.price
price


# In[7]:


reg = linear_model.LinearRegression()
reg.fit(new_df,price)


# In[8]:


reg.predict([[3300]])


# In[9]:


reg.coef_


# In[10]:


reg.intercept_


# In[11]:


3300*135.78767123 + 180616.43835616432


# In[12]:


reg.predict([[5000]])


# In[14]:


area_df = pd.read_csv("https://raw.githubusercontent.com/charanbhc/py/master/ML/1_linear_reg/areas.csv")
area_df.head(3)


# In[15]:


p = reg.predict(area_df)
p


# In[16]:


area_df['prices']=p
area_df


# In[17]:


area_df.to_csv("https://raw.githubusercontent.com/charanbhc/py/master/ML/1_linear_reg/prediction.csv")


# In[ ]:




