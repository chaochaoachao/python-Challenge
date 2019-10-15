#!/usr/bin/env python
# coding: utf-8

# In[1]:

# Dependencies
import pandas as pd
import numpy as np

# In[2]:

#find filepath
filepath="Resources/budget_data.csv"
#load csv
pybank_data=pd.read_csv(filepath)
#pybank_data


# In[3]:


#unique() to make sure they are no repeated months
total_month=len(pybank_data["Date"].unique())
#total_month


# In[4]:


Totals=pybank_data["Profit/Losses"].sum()
#Totals


# In[5]:


#Create a new column "change" and shift it down by 1 row
pybank_data["change"]=pybank_data["Profit/Losses"].diff(periods=-1)*-1
pybank_data["change"]=pybank_data["change"].shift(1)
#pybank_data

# In[6]:


average_change=pybank_data["change"].mean()
#average_change


# In[7]:


#using pandas loc will give an object, use item() to get the date without index
Greatest_Increase_in_Profits=pybank_data["change"].max()
Greatest_Increase_month=pybank_data["Date"].loc[pybank_data["change"] ==Greatest_Increase_in_Profits].item()
#Greatest_Increase_month


# In[8]:

Greatest_Decrease_in_Profits=pybank_data["change"].min()
Greatest_Decrease_month=pybank_data["Date"].loc[pybank_data["change"] ==Greatest_Decrease_in_Profits].item()
#Greatest_Decrease_month

# In[9]:
#print all results 

import sys
f = open("Financial Analysis.txt", 'w')
sys.stdout = f

print("Financial Analysis")
print("----------------------")
print("Total Month:",total_month)
print("Total: $",Totals)
print("Average  Change: $",average_change)
print("Greatest Increase in Profits: "+str(Greatest_Increase_month)+"($"+str(pybank_data["change"].max())+")")
print("Greatest Decrease in Profits: "+str(Greatest_Decrease_month)+"($"+str(pybank_data["change"].min())+")")


f.close()