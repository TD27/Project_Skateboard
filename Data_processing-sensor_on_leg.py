#!/usr/bin/env python
# coding: utf-8

# # Sensor on leg
# Purpose of this experiment is to survey a motion of the skateboard during a skateboard trick called **Ollie**. I measure two physical quantities: gyroscope speed [rad/s] and acceleration [m/s^2]. Each quantity is represented by its x,y,z component. A smartphone and its app Phyphox works as a sensor estimating and calculating the movement and provides data to xls files. The smartphone was stuck on my leg. I made ten attempts.

# The script that is processing data is written in Python. I use popular libraries such as: Pandas, NumPy, and Matplolib

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# Experiment consists of 10 measurements. 

# In[2]:


VideoTimeOfTheExperiement = {
    "Exp1" : "0.19",
    "Exp2" : "1.20",
    "Exp3" : "2:20",
    "Exp4(5)" : "3:07",
    "Exp5" : "4:20",
    "Exp6(7)" : "5:35",
    "Exp7(8)" : "6:30",
    "Exp8(9)" : "7:15",
    "Exp9(10)" : "7:55",
    "Exp10(11)" : "8:35 "
}

URLKeys_Leg = {
    "Exp2" : "1jpkzzOPKSsxLzvqVpLwdUXHt7x_zDcQB",
    "Exp3" : "19LX_0Se2VrXdYUOwJQ6AJAmw0pG_iapv",
    "Exp4(5)" : "1QZ3Kd34F7ozO8-LZ8de__tSvdl9RzSTC",
    "Exp5" : "1FvSAAIozBszLYqiX12ms9RBzPSFazGnI",
    "Exp6(7)" : "1zs0ss59yLM1xqoOKM5BgZ0b0u-GRln24",
    "Exp7(8)" : "1bMeB7DgIvmBkN5g99PVUe1VFHdDDFNqE",
    "Exp8(9)" : "1pMKuiQ94n1lzXFSwPEFuVZ2aHYE2vy1-",
    "Exp9(10)" : "1Ri5iHWYBIgz8tGcbQKl8oyyJd7YBJJ0h",
    "Exp10(11)" : "1X4FWFzKxU47NVt250Gr-X45jjbo8c8Fb"
}


# Each attempt takes 20 seconds, but only 2-3 seconds are vital. Following "ranges" focus on the most critical data for further analysis.

# In[3]:


Ranges = {
    "Exp2" : [4500,5500],
    "Exp3" : [4500,6000],
    "Exp4(5)" : [4500,5500],
    "Exp5" : [4000,5500],
    "Exp6(7)" : [4000,5000],
    "Exp7(8)" : [3500,5000],
    "Exp8(9)" : [4500,6000],
    "Exp9(10)" : [3000,4000],
    "Exp10(11)" : [6000,7500]
}


# This script downloads data from Google Sheets, converts headers and plots data into the graphs. Each attempt has two graphs: Gyroscope and Accelerometer. 

# In[4]:


for i in URLKeys_Leg:
    GoogleSheetID=URLKeys_Leg[i]
    WorksheetName='Gyroscope'
    path='https://docs.google.com/spreadsheets/d/{0}/gviz/tq?tqx=out:csv&sheet={1}'.format(
        GoogleSheetID,
        WorksheetName
    )
    
    data_Gyr = pd.read_csv(path)
    
    data_Gyr.columns = [c.replace(' ', '_') for c in data_Gyr.columns]
    data_Gyr.columns = [c.replace('_(rad/s)', '') for c in data_Gyr.columns]
    data_Gyr.columns = [c.replace('_(s)', '') for c in data_Gyr.columns]
    
    
    GoogleSheetID=URLKeys_Leg[i]
    WorksheetName='Accelerometer'
    path='https://docs.google.com/spreadsheets/d/{0}/gviz/tq?tqx=out:csv&sheet={1}'.format(
        GoogleSheetID,
        WorksheetName
    )
    
    data_Acc = pd.read_csv(path)
    
    data_Acc.columns = [c.replace(' ', '_') for c in data_Acc.columns]
    data_Acc.columns = [c.replace('_(m/s^2)', '') for c in data_Acc.columns]
    data_Acc.columns = [c.replace('_(s)', '') for c in data_Acc.columns]
    
    
    a,b=Ranges[i]
    
    graphdata_Gyr=data_Gyr.loc[a:b,:]
    graphdata_Acc=data_Acc.loc[a:b,:]
    
    Title=i+" Gyroscope"      
    plt.figure(figsize=(15,5))
    plt.title(Title)
    plt.plot(graphdata_Gyr.Time, graphdata_Gyr.Gyroscope_x, color="red")
    plt.plot(graphdata_Gyr.Time, graphdata_Gyr.Gyroscope_y, color="blue")
    plt.plot(graphdata_Gyr.Time, graphdata_Gyr.Gyroscope_z, color="green")

    Title=i+" Accelerometer"      
    plt.figure(figsize=(15,5))
    plt.title(Title)
    plt.plot(graphdata_Acc.Time, graphdata_Acc.Acceleration_x, color="red")
    plt.plot(graphdata_Acc.Time, graphdata_Acc.Acceleration_y, color="blue")
#    plt.plot(graphdata_Acc.Time, graphdata_Acc.Acceleration_z, color="green")
    
    plt.show()


# In[ ]:





# In[ ]:




