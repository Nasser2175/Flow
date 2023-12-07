#!/usr/bin/env python
# coding: utf-8

# In[15]:


import pandas as pd

# Replace 'your_file.csv' with the actual file path
file_path = 'inflow.csv'

# Use pandas to read the CSV file
Flow = pd.read_csv(file_path)

# Display the DataFrame
print(Flow)


# ### Minimum Night Flow (MNF) analysis between 2 to 4 oclock

# In[8]:


MNF = pd.read_csv("inflow.csv", index_col=0, parse_dates=[0], header=0)
MNF=MNF.between_time('2:00', '4:00').resample("1D").mean()
MNF


# ## Calculating the average flow between 02:00 and 04:00 in the night for each day and plotting the data

# In[11]:


MNF= pd.read_csv("inflow.csv", index_col=0, parse_dates=[0], header=0)
MNF =MNF.between_time('2:00', '4:00').resample("1D").mean()
MNF.plot(figsize=(18,8))
MNF['0'].rolling(window='7D').mean().plot(figsize=(18,8))


# In[18]:


MNF = pd.read_csv("inflow.csv", index_col=0, parse_dates=[0], header=0)
MNF=MNF.between_time('1:00', '3:00').resample("1D").mean()
MNF


# # Calculating the average flow between 01:00 and 03:00 in the night for each day and plotting the data

# In[13]:


MNF= pd.read_csv("inflow.csv", index_col=0, parse_dates=[0], header=0)
MNF =MNF.between_time('1:00', '3:00').resample("1D").mean()
MNF.plot(figsize=(18,8))
MNF['0'].rolling(window='7D').mean().plot(figsize=(18,8))


# # Moving avarage

# In[26]:



import matplotlib.pyplot as plt  # Don't forget to import matplotlib.pyplot

# Load flow data (replace 'inflow.csv' with your actual file path)
_MNF = pd.read_csv("inflow.csv", index_col=0, parse_dates=[0], header=0)

# Plot the flow data
_MNF['0'].plot(figsize=(18, 8), label='Flow Data')
_MNF['0'].rolling(window='7D').mean().plot(label='7-Day Rolling Mean')
plt.legend()
plt.show()


# In[ ]:


pip install streamlit pandas matplotlib
streamlit run app.py
conda install -c conda-forge streamlit


# In[ ]:


conda install -c anaconda numexpr=2.7.3


# In[ ]:




