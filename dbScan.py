#DBSCAN Clustering 
#not fully complete 7/5/21

import pandas as pd
import numpy as np

import itertools
import sklearn as sk
from datetime import datetime, timedelta
import time
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn import metrics
from sklearn.cluster import KMeans
from sklearn.cluster import DBSCAN
from sklearn.preprocessing import StandardScaler

import matplotlib.pyplot as plt

from scipy.stats import entropy
from sklearn.neighbors import NearestNeighbors
from scipy.optimize import linear_sum_assignment



#================================================================================================================ 
#Get Columns from Signal Data CSV file
#================================================================================================================

col_list = ["TimeStamp", "DeviceId", "EventId", "Parameter"]
df = pd.read_csv('Signal_events.txt', delimiter = " ")


df["TimeStamp"] = pd.to_datetime(df["TimeStamp"])
pd.to_datetime(df["TimeStamp"])

time_series= df['TimeStamp']


#parameter_series = df_spat["Parameter"]

#event_par_df = pd.DataFrame(event_id_series)

print(df.head())

print(df.info())

print(df.describe())

df.drop(columns = ['TimeStamp', 'DeviceId'], axis = 1, inplace=True)

print(df.head(1000))

#X = event_par_df

#db = DBSCAN(eps=4, min_samples=5).fit(X)

#dbs_clustering_labels = db.labels_\


x = df["EventId"]

y = df["Parameter"]

plt.scatter(x,y, cmap='viridis')

plt.xlabel("Event_ID")

plt.ylabel("Parameter")

plt.title("DB-Scan")

plt.show()


df = df[["EventId", "Parameter"]]
df = df.values.astype("float32", copy = False)

stscaler = StandardScaler().fit(df)

df = stscaler.transform(df)

dbsc = DBSCAN(eps = 0.5, min_samples = 15).fit(df)

labels = dbsc.labels_

core_samples = np.zeros_like(labels, dtype = bool)
core_samples[dbsc.core_sample_indices_] = True

spat=list(core_samples)

df0 = pd.read_csv('Signal_events.txt', delimiter = " ")

df0.drop(columns = ['TimeStamp', 'DeviceId'], axis = 1, inplace=True)

#add code to randomize df0

df0["spat"]=spat

#randomize

#sns.lmplot("EventId","Parameter",data=df0,fit_reg=False,hue="spat",height=10)

#plt.show()
