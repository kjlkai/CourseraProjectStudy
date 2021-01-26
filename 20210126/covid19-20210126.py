#!/usr/bin/env python
# coding: utf-8

# # Welcome to Covid19 Data Analysis Notebook
# ------------------------------------------

# ### Let's Import the modules 

# In[20]:


import pandas as pd 
import numpy as np 
import seaborn as sns
import matplotlib.pyplot as plt 
print('Modules are imported.')


# ## Task 2 

# ### Task 2.1: importing covid19 dataset
# importing "Covid19_Confirmed_dataset.csv" from "./Dataset" folder. 
# 

# In[21]:


corona_dataset_csv = pd.read_csv("Datasets/covid19_Confirmed_dataset.csv")
corona_dataset_csv.head(10)


# #### Let's check the shape of the dataframe

# In[22]:


corona_dataset_csv.shape


# ### Task 2.2: Delete the useless columns

# In[23]:


corona_dataset_csv.drop(["Lat","Long"],axis=1, inplace=True)


# In[24]:


corona_dataset_csv.head(10)


# ### Task 2.3: Aggregating the rows by the country

# In[27]:


corona_dataset_aggregated = corona_dataset_csv.groupby("Country/Region").sum()


# In[30]:


corona_dataset_aggregated.head(10)


# In[31]:


corona_dataset_aggregated.shape


# ### Task 2.4: Visualizing data related to a country for example China
# visualization always helps for better understanding of our data.

# In[34]:


corona_dataset_aggregated.loc["China"].plot()
corona_dataset_aggregated.loc["Italy"].plot()
corona_dataset_aggregated.loc["Spain"].plot()
plt.legend()


# ### Task3: Calculating a good measure 
# we need to find a good measure reperestend as a number, describing the spread of the virus in a country. 

# In[35]:


corona_dataset_aggregated.loc['China'].plot()


# In[36]:


corona_dataset_aggregated.loc["China"][:3].plot()


# ### task 3.1: caculating the first derivative of the curve

# In[37]:


corona_dataset_aggregated.loc["China"].diff().plot()


# ### task 3.2: find maxmimum infection rate for China

# In[38]:


corona_dataset_aggregated.loc["China"].diff().max()


# In[39]:


corona_dataset_aggregated.loc["Italy"].diff().max()


# In[40]:


corona_dataset_aggregated.loc["Spain"].diff().max()


# ### Task 3.3: find maximum infection rate for all of the countries. 

# In[58]:


countries = list(corona_dataset_aggregated.index)
max_infection_rates = []
for c in countries :
    max_infection_rates.append(corona_dataset_aggregated.loc[c].diff().max())
corona_dataset_aggregated["max_infection_rate"] = max_infection_rates


# In[61]:


corona_dataset_aggregated.head()


# ### Task 3.4: create a new dataframe with only needed column 

# In[64]:


corona_data = pd.DataFrame(corona_dataset_aggregated["max_infection_rate"])


# In[65]:


corona_data.head()


# ### Task4: 
# - Importing the WorldHappinessReport.csv dataset
# - selecting needed columns for our analysis 
# - join the datasets 
# - calculate the correlations as the result of our analysis

# ### Task 4.1 : importing the dataset

# In[66]:


happiness_report_csv = pd.read_csv("Datasets/worldwide_happiness_report.csv")


# In[67]:


happiness_report_csv.head()


# ### Task 4.2: let's drop the useless columns 

# In[68]:


useless_cols = ["Overall rank","Score","Generosity","Perceptions of corruption"]


# In[70]:


happiness_report_csv.drop(useless_cols, axis=1, inplace=True)
happiness_report_csv.head()


# ### Task 4.3: changing the indices of the dataframe

# In[72]:


happiness_report_csv.set_index("Country or region", inplace = True)


# In[74]:


happiness_report_csv.head()


# ### Task4.4: now let's join two dataset we have prepared  

# #### Corona Dataset :

# In[77]:


corona_data.head()


# In[78]:


corona_data.shape


# #### wolrd happiness report Dataset :

# In[79]:


happiness_report_csv.head()


# In[80]:


happiness_report_csv.shape


# In[81]:


data = corona_data.join(happiness_report_csv, how="inner")
data.head()


# ### Task 4.5: correlation matrix 

# In[82]:


data.corr()


# ### Task 5: Visualization of the results
# our Analysis is not finished unless we visualize the results in terms figures and graphs so that everyone can understand what you get out of our analysis

# In[83]:


data.head()


# ### Task 5.1: Plotting GDP vs maximum Infection rate

# In[86]:


x = data["GDP per capita"]
y = data["max_infection_rate"]
sns.scatterplot(x,np.log(y))


# In[87]:


sns.regplot(x, np.log(y))


# ### Task 5.2: Plotting Social support vs maximum Infection rate

# In[89]:


x = data["GDP per capita"]
y = data["Social support"]
sns.scatterplot(x,np.log(y))


# In[90]:


sns.regplot(x, np.log(y))


# ### Task 5.3: Plotting Healthy life expectancy vs maximum Infection rate

# In[91]:


x = data["GDP per capita"]
y = data["Healthy life expectancy"]
sns.scatterplot(x,np.log(y))


# In[92]:


sns.regplot(x, np.log(y))


# ### Task 5.4: Plotting Freedom to make life choices vs maximum Infection rate

# In[94]:


x = data["GDP per capita"]
y = data["Freedom to make life choices"]
sns.scatterplot(x,np.log(y))


# In[95]:


sns.regplot(x, np.log(y))


# In[ ]:




