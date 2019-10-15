#!/usr/bin/env python
# coding: utf-8

# In[1]:

# Dependencies
import pandas as pd
import numpy as np

# In[17]:
filepath="Resources/election_data.csv"
pypoll_data=pd.read_csv(filepath)
#pypoll_data

# In[9]:

Total_votes=len(pypoll_data["Voter ID"].unique())

# In[12]:

pypoll_data["Candidate"].unique()


# In[25]:

candidate_data=pypoll_data.Candidate.value_counts()
#candidate_data

# In[23]:

#check votes
pypoll_data.Candidate.value_counts().sum()-Total_votes

# In[41]:

candidate_data_frame=candidate_data.to_frame()
candidate_data_frame["Percentage"]=candidate_data_frame["Candidate"]/Total_votes*100
candidate_data_frame["Percentage"]=candidate_data_frame["Percentage"].round(3).astype(str)+"%"

#candidate_data_frame


# In[68]:

#candidate_data_frame.style.format({'Candidate': '{:,.3%}','percent': '{:,.3%}'})
candidate_data_frame["Name"]=candidate_data_frame.index

#candidate_data_frame


# In[77]:


winner=candidate_data_frame["Name"].loc[candidate_data_frame["Candidate"]==candidate_data_frame["Candidate"].max()]


# In[79]: rename the index of dataframe and print all results
poll_result=candidate_data_frame.rename(columns={'Candidate':'Votes'})

winner.item()
import sys
f = open("election-result.txt", 'w')
sys.stdout = f
print("Election Results")
print("----------------------")
print("Total Votes:",Total_votes)
print("----------------------")
print(poll_result[['Votes',"Percentage"]])
print("----------------------")
print("winner",winner.item() )
print("----------------------")
f.close()



#%%
