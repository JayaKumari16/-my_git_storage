#!/usr/bin/env python
# coding: utf-8

# Write a Python program using Scikit-learn to split the iris dataset into 80% train data and 20% test data.
# Out of total 150 records, the training set will contain 120 records and the test set contains 30 of those records. 
# Train or fit the data into the model and calculate the accuracy of the model using the Random Forest Classifier Algorithm.

# In[28]:


import pandas as pd
import seaborn as sns
df=sns.load_dataset('iris')  


# In[29]:


df


# In[30]:


from sklearn.datasets import load_iris


# In[81]:


iris_data = load_iris() 
iris_data


# In[84]:


iris=pd.DataFrame(iris_data.data)
iris_data.data


# In[85]:


type(df)


# In[86]:


print(iris_data.target_names)


# In[87]:


print(iris_data.feature_names)


# In[88]:


iris


# In[89]:


df.info()


# In[91]:


df.corr()


# In[105]:


df1=df.drop('species',axis=1)
for i in df1:
    sns.boxplot(df1[i])


# In[92]:


df['sepal_length'].value_counts


# In[93]:


df['petal_length'].value_counts


# In[94]:


sns.heatmap(df.corr(),annot=True)


# In[95]:


df.head(10)


# In[96]:


df.isnull().sum()


# In[97]:


df.duplicated()


# In[98]:


x=df[['sepal_length','sepal_width','petal_length','petal_width']]
x


# In[99]:


y=df['species']
y


# In[100]:


from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2)


# In[67]:


x_train.shape,x_test.shape,y_train.shape,y_test.shape


# In[72]:


from sklearn.ensemble import RandomForestClassifier


# In[75]:


clf=RandomForestClassifier(random_state=100)


# In[76]:


clf.fit(x_train,y_train)


# In[77]:


pred=clf.predict(x_test)


# In[78]:


#Import scikit-learn metrics module for accuracy testing
from sklearn import metrics


# In[79]:


print("Accuracy:",metrics.accuracy_score(y_test,pred))


# In[ ]:




