import pandas as pd
import numpy as np
import sklearn as sk
from datetime import datetime, timedelta
import time
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
import matplotlib.pyplot as plt
import seaborn as sns



#================================================================================================================ 
#Get Columns from Signal Data CSV file
#================================================================================================================

col_list = ["TimeStamp", "DeviceId", "EventId", "Parameter"]
df_spat = pd.read_csv('Signal_events.txt', delimiter = " ")


df_spat["TimeStamp"] = pd.to_datetime(df_spat["TimeStamp"])
time = pd.to_datetime(df_spat["TimeStamp"])
#print (df_spat)

eventid = df_spat['EventId']
parameter = df_spat['Parameter']
new_time = []
for row in range(len(time)):
    
    new_time.append((time[row] - datetime(2021, 1,4)).total_seconds())

#print(new_time)

spat = []

for i in range(len(df_spat)//1000):
    
    spat.append((1000*i, eventid[1000*i], parameter[1000*i]))
    

#line_df = pd.DataFrame(data=spat, columns = ["time", "eventid", "parameter"])
#print(line_df)
            

#lineplot = sns.lineplot(data=line_df, x= "time" , y = "eventid", hue = "parameter" )
#plt.yticks(np.arange(0,100, step =5))
#plt.ylim(0,100)

#plt.xlabel("timestamp")
#plt.ylabel("eventId")


#grouped = df_spat.groupby(["Parameter"], sort = True)

#bins = [0, 3, 6, 9, 12, 15, 18, 21, 24]

#labels = ["00:00-02:59","3:00-5:59", "06:00-8:59","9:00-11:59", "12:00-14:59","15:00-17:59", "18:00-20:59", "21:00-23:59"]

bins = [1,2,3,4,5, 6,7, 8,9,10, 11, 12,13, 14,15, 16, 17, 18,19, 20,21,22,23, 24]

labels = ["0-1", "1-2", "2-3", "3-4", "4-5", "5-6", "6-7", "7-8", "8-9", "9-10", "11-12", "12-13"
         , "13-14", "14-15", "15-16", "16-17", "17-18","18-19", "19-20", "20-21", "21-22", "22-23","23-24"]


df_spat["TimeStamp"] = pd.cut(df_spat.TimeStamp.dt.hour, bins, labels = labels, right=False)

x,y = 'TimeStamp', 'Parameter'

df_y = df_spat.groupby(x)[y].value_counts(normalize = True)
df_y = df_y.mul(100)
df_y = df_y.rename('Percent').reset_index()



#fig, barchart = plt.subplots()

barchart = sns.catplot(x=x, y='Percent', hue=y, kind='bar', data=df_y)
barchart.ax.set_ylim(0,25)
plt.xticks(rotation=45)

def change_width(ax, new_value) :
    for patch in ax.patches :
        current_width = patch.get_width()
        diff = current_width - new_value

        # we change the bar width
        patch.set_width(new_value)

        # we recenter the bar
        patch.set_x(patch.get_x() + diff * .5)

#change_width(barchart, .35)

#plt.figure(figsize=(100,50))

plt.title("Percentage in Parameter vs. Time")

plt.show()
