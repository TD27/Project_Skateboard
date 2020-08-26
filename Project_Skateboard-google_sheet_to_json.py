#!/usr/bin/env python
# coding: utf-8

# # Sensor on leg

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import json
from jsonmerge import Merger


# In[2]:


video_time = {
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

URL_keys_leg = {
    "Exp2" : '1u2JN_yVS9I-aDDk-xtRFLs9SDdrUNo0f',
    "Exp3" : '1qolBHxLSiGi-bmDUZ-V0WzaCay7UaA3x',
    "Exp4(5)" : '1eEh3oZpFoCo4dGdcVoGH6kuwIe7QY6rr',
    "Exp5" : '1P3E_T65CdJncewSVA-3H8hveejoqcdy4',
    "Exp6(7)" : '1kFniM6vHQVy659t0I4R86xH6bfGgo97K',
    "Exp7(8)" : '19j6veOIvJoe3aln1MURMChglvMA2F5AS',
    "Exp8(9)" : '1akmRWg8bhkKlAQV0XimEPTzsa7_UvazU',
    "Exp9(10)" : '1llYUn_deIMOUQl14-aJL9Gw5BqT3nH53',
    "Exp10(11)" : '1hdnEeKw7eb2bEvJLbtd12irF3N5qIFmc'
}

URL_keys_skateboard = {
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

URL_keys = {
    "skateboard" : URL_keys_skateboard,
    "leg" : URL_keys_leg
}


# In[3]:


ranges = {
    "Exp2" : [500,900],
    "Exp3" : [600,1000],
    "Exp4(5)" : [600,1000],
    "Exp5" : [600,1000],
    "Exp6(7)" : [600,1000],
    "Exp7(8)" : [550,950],
    "Exp8(9)" : [700,1100],
    "Exp9(10)" : [1250,1750],
    "Exp10(11)" : [700,1100]
}

classification = {
    "Exp2" : "good",
    "Exp3" : "bad",
    "Exp4(5)" : "good",
    "Exp5" : "good",
    "Exp6(7)" : "bad",
    "Exp7(8)" : "good",
    "Exp8(9)" : "good",
    "Exp9(10)" : "bad",
    "Exp10(11)" : "good"
}


# In[4]:


def to_json (data):
    result=data.to_json(orient="split")
    parsed=json.loads(result)
    file=json.dumps(parsed,indent=4)
    return file

def import_from_google (ID,name):
    google_sheet_ID=ID
    work_sheet=name
    path='https://docs.google.com/spreadsheets/d/{0}/gviz/tq?tqx=out:csv&sheet={1}'.format(
        google_sheet_ID,
        work_sheet
    )

    data = pd.read_csv(path)

    data.columns = [c.replace(' ', '_') for c in data.columns]
    data.columns = [c.replace('_(rad/s)', '') for c in data.columns]
    data.columns = [c.replace('_(s)', '') for c in data.columns]
    
    return data


# In[7]:


for j in URL_keys.keys():
    print("j=",j)
    for i in URL_keys[j]:
        print("i=",i)
        data_gyr=import_from_google(URL_keys[j][i],'Gyroscope')
        data_acc=import_from_google(URL_keys[j][i],'Accelerometer')
        print(URL_keys[j][i])

        experiment_header = {
            "experiment_name" : i,
            "video_time" : video_time[i],
            "URL_key" : URL_keys[j][i],
            "sensor" : j,
            "classification" : classification[i]
        }

        json1=to_json(data_gyr)
        json2=to_json(data_acc)
        json3=json.dumps(experiment_header,indent=4)

        json_result=""

        json_result += json3
        json_result += json1
        json_result += json2

        m = open(j+"_"+i+".json", "w")
        m.write(json_result)
        m.close()    


# json merge: https://pypi.org/project/jsonmerge/

# In[ ]:




