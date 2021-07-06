#KMeans Clustering 

import matplotlib.pyplot as plt
%matplotlib inline
import numpy as np
from sklearn.cluster import KMeans
import pandas as pd
import itertools

#Read from signal file

col_list = ["TimeStamp", "DeviceId", "EventId", "Parameter"]
df = pd.read_csv('Signal_events.txt', delimiter = " ")


df["TimeStamp"] = pd.to_datetime(df["TimeStamp"])
pd.to_datetime(df["TimeStamp"])

time_series= df['TimeStamp']



print(df.head())

print(df.info())

print(df.describe())

df.drop(columns = ['TimeStamp', 'DeviceId'], axis = 1, inplace=True)

df = df.drop(labels=0, axis=0)

#print(df.head(100))

df = df.head(100)

#split for clusters

Xpts = df["EventId"]
Ypts = df["Parameter"]


Points = np.array(list(itertools.product(Xpts, Ypts)))

#append to numpy array

print(Points)


#for item in result:
    #result[0][0] = float(result[0][0])
    #result[1][1] = float(result[1][1])
    



#print(new_arr)

#for tup in result:
    #np.append(new_arr, tup, axis = 0)
    
#print(new_arr)
    

#result_float = [float(x) for x in result]

print(result)



#print(arr)

#for item in result:
    #column_to_be_added = np.array(item)
    #np.hstack((arr, np.atleast_2d(column_to_be_added)))
    
#arr = np.array(result)
    
X = Points

print(X)

                  
plt.scatter(x,y, label='True Position')
#plt.show()


# K MEANS CLUSTERING 

n_clusters = 8
kmeans = KMeans(n_clusters=8)
kmeans.fit(X)



print(kmeans.cluster_centers_)

print(kmeans.labels_)

print("K-Means with # clusters = ")
print(n_clusters)

plt.scatter(X[:,0],X[:,1], c=kmeans.labels_, cmap='rainbow')


plt.scatter(X[:,0],X[:,1], c=kmeans.labels_, cmap='rainbow')
plt.scatter(kmeans.cluster_centers_[:,0] ,kmeans.cluster_centers_[:,1], color='black')

plt.xlabel("EventId")

plt.ylabel("Parameter")

plt.title("K-Means Clustering")
