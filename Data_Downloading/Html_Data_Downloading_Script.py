# -*- coding: utf-8 -*-
"""
Created on Sun Jul 19 23:34:21 2020

@author: mohit
"""
import os
import time
import requests #to request particular url
import sys
# Bangalore: 432950
# Delhi/Palam: 421810
# Lucknow: 423690
def retrieve_html(start = 2015, end = 2019):
    for year in range(start, end + 1):
        for month in range(1,13):
            if(month<10):
                url='http://en.tutiempo.net/climate/0{}-{}/ws-421810.html'.format(month
                                                                          ,year)
            else:
                url='http://en.tutiempo.net/climate/{}-{}/ws-421810.html'.format(month
                                                                          ,year)
            texts=requests.get(url)
            text_utf=texts.text.encode('utf=8').strip() # utf encoding
            
            if not os.path.exists("Data/Html_Data/{}".format(year)):
                os.makedirs("Data/Html_Data/{}".format(year))
            with open("Data/Html_Data/{}/{}.html".format(year,month),"wb") as output:
                output.write(text_utf)
            
        sys.stdout.flush()


if __name__=="__main__":
    start_time=time.time()
    retrieve_html()
    stop_time=time.time()
    print("Time taken {}".format(stop_time-start_time))