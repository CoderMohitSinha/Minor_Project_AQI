#!/usr/bin/env python
# coding: utf-8

# In[69]:


## importing packages
import numpy as np
import pandas as pd
import requests
import sys
import os
import csv
from bs4 import BeautifulSoup 


# In[70]:



def met_data(month, year):
    
    file_html = open('Data/Html_Data/{}/{}.html'.format(year,month), 'rb')
    plain_text = file_html.read()

    tempD = [] # temp data
    finalD = [] # final data

    soup = BeautifulSoup(plain_text, "lxml")
    for table in soup.findAll('table', {'class': 'medias mensuales numspan'}):
        for tbody in table:
            for tr in tbody:
                a = tr.get_text()
                tempD.append(a)

    rows = len(tempD) / 15
    # 15 features
    for times in range(round(rows)):
        newtempD = []
        for i in range(15):
            newtempD.append(tempD[0])
            tempD.pop(0)
        finalD.append(newtempD)

    length = len(finalD)

    finalD.pop(length - 1)
    finalD.pop(0)

    for a in range(len(finalD)):
        if len(finalD[a]) >= 15:
            finalD[a].pop(14)
            finalD[a].pop(13)
            finalD[a].pop(12)
            finalD[a].pop(11)
            finalD[a].pop(10)
            finalD[a].pop(9)
            finalD[a].pop(6)
            finalD[a].pop(4)
            finalD[a].pop(0)
        elif len(finalD[a]) >= 14:
            finalD[a].pop(13)
            finalD[a].pop(12)
            finalD[a].pop(11)
            finalD[a].pop(10)
            finalD[a].pop(9)
            finalD[a].pop(6)
            finalD[a].pop(4)
            finalD[a].pop(0)
        

    return finalD


# In[71]:


def data_combine(year, cs):
    for a in pd.read_csv('Data/Real-Data/real_' + str(year) + '.csv', chunksize=cs):
        df = pd.DataFrame(data=a)
        mylist = df.values.tolist()
    return mylist


# In[72]:


if __name__ == "__main__":
    total_data = []
    if not os.path.exists("Data/Real-Data"):
        os.makedirs("Data/Real-Data")
    for year in range(2015, 2020):
        final_data = []
        for month in range(1, 13):
            temp = met_data(month, year)
            final_data = final_data + temp
        total_data = total_data + final_data


# In[73]:


total_data


# In[74]:


PATH_CITY_DAY = "C:/Users/mohit/Documents/Minor_Project/Temp_Other_Data/Kaggle_AQI/city_day.csv"
df = pd.read_csv(PATH_CITY_DAY)
df = df[9540:11366] ## row number in data file
lst = np.array(df['AQI'])
lst = lst.tolist()
lst


# In[75]:


len(total_data)


# In[76]:


len(lst)


# In[77]:


for i in range(len(total_data)):
        # final[i].insert(0, i + 1)
        total_data[i].insert(7, lst[i])


# In[78]:


total_data


# In[90]:


# with open('Data/Real-Data/Real_Combine.csv', 'w') as csvfile:
#         wr = csv.writer(csvfile, dialect='excel')
#         wr.writerow(
#             ['T', 'TM', 'Tm', 'SLP', 'H', 'VV', 'V', 'VM', 'PM 2.5'])
with open('Data/Real-Data/Real_Combine.csv', 'w') as csvfile:
            wr = csv.writer(csvfile, dialect='excel', )
            for row in total_data:
                flag = 0
                for elem in row:
                    if elem == "" or elem == "-":
                        flag = 1
                if flag != 1:
#                     print(1)
                    wr.writerow(row)


# In[92]:


df=pd.read_csv('Data/Real-Data/Real_Combine.csv', header=None)
df


# In[100]:


df.to_csv("Data/Real-Data/Real_Combine.csv", header=["T", "TM", "Tm", "H", "VV", "V", "PM2.5"], index=False)
df



