import pandas as pd   #numpy, scify, cython, matplotlib, windows = set of application, Application Platform Interface
import numpy as np

K = np.array([1.8, 'f', 4, 'h', '6', 'g', 'n', 'r' ,'d'])
y = pd.Series(K) #How to create a series

y


# In[42]:


x = ["Bed Prakash Das", "Ishan Mitra", "Tushan Mitra"]
z = pd.DataFrame(x)   #creating a dataframe constructor on a list of strings


# In[43]:


z


# In[44]:


a = {"Bed Prakash Das":3, "Ishan Mitra":4, "Tushan Mitra":2}  #Creating a data dictonary
a1 = pd.Series(a)


# In[45]:


a1[0]


# In[46]:


a2 = pd.Series(4, index = [0, 1, 2])
a2


# In[47]:


a1.index #index and values of the data dictionary


# In[48]:


a1.values #


# In[49]:


a1.item


# In[50]:


a2.items


# In[51]:


a=pd.Series(data=[1,2,3,np.NaN])
b=pd.Series(data=[4.9,8.2,5.6],index=['x','y','z'])
c=pd.Series()
print(a.empty,b.empty,c.empty)
print(a.hasnans,b.hasnans,c.hasnans)
print(len(a),len(b))
print(a.count( ),b.count( ))


# In[52]:


a


# In[53]:


b


# In[54]:


a.empty


# In[55]:


c.empty


# In[56]:


a.hasnans


# In[57]:


b.hasnans


# In[58]:


len(a)


# In[59]:


len(b)


# In[60]:


len(c)


# In[61]:


b.count()


# In[62]:


# program to tabulate the marks of three students in a dataframe
d = {'Name':["Bed Prakash Das", "Tushan Mitra", "Ishan Mitra"], 'Subject1':[45, 47, 48], 'Subject2':[47, 50, 44], 'Subject3':[44, 44, 44]}
s = pd.DataFrame(d)


# In[63]:


s


# In[64]:


de = {'Name':["Bed Prakash Das", "Ishan Mitra", "Tushan Mitra"], 'Age':["No Data", 10, 6], 'Nickname':["No Data", "No Data", "No Data"]}
tab = pd.DataFrame(de)
pd.ExcelWriter('Name.xlsx', engine = 'xlsxwriter')


# In[65]:


tab


# In[66]:


pd.Timestamp('2020,80,10')


# In[67]:


pd.Timestamp('2020-10-08T16')


# In[68]:


path = 'C:\Files\Ishan\Pandas.xlsx'
pd.ExcelWriter(path, engine = 'xlsxwriter')


# In[69]:


import xlwt


# In[70]:


df = pd.DataFrame({'Data': [10, 20, 30, 20, 15, 30, 45]})
w = pd.ExcelWriter('Pandas.xlsx', engine='xlsxwriter')
tab.to_excel(w, sheet_name='Sheet1')
w.save()
