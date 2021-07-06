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
#Get Columns from SPaT CSV file with Phase, Result, Start, End, Duration
#================================================================================================================

col_list = ['Phase', 'Result', 'Start', 'End', 'Duration']
df_spat = pd.read_csv('format4_sklearn_dataset_with_duration.csv', usecols = col_list)


df_spat["TimeStamp"] = pd.to_datetime(df_spat["Start"])


bins = [1,2,3,4,5, 6,7, 8,9,10, 11, 12,13, 14,15, 16, 17, 18,19, 20,21,22,23, 24]

labels = ["0-1", "1-2", "2-3", "3-4", "4-5", "5-6", "6-7", "7-8", "8-9", "9-10", "11-12", "12-13"
         , "13-14", "14-15", "15-16", "16-17", "17-18","18-19", "19-20", "20-21", "21-22", "22-23","23-24"]

df_spat["TimeStamp"] = pd.cut(df_spat.TimeStamp.dt.hour, bins, labels = labels, right=False)

x,y,z = 'TimeStamp', 'Phase', 'Duration'

#df_spat[z] = max(df_spat[z].value_counts())

#print(df)

plt.figure(figsize=(20,10))

#barchart = sns.catplot(x=x, y=z, hue=y, kind='swarm', data=df_spat)
#barchart.ax.set_ylim(0,100)

plt.title("Phase and Duration vs. Time")


linechart = sns.lineplot(data=df_spat, x="TimeStamp", y= "Duration", hue = "Phase" )

plt.show()
