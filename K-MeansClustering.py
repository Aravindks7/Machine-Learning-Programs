import pandas as pd
import numpy as np
from sklearn.cluster import KMeans


df = pd.read_csv('https://gist.githubusercontent.com/net/8836201/raw/6f9306ad21398ea43cba4f7d537619d0e07d5ae3/iris.csv') 
df
df['variety'].unique()


real_target = df.pop('variety') 
real_target.replace({ 'Setosa':0,
                     'Virginica':2,
                     'Versicolor':1}, inplace=True)


model KMeans (n_clusters=3) 
target_predict = model.fit_predict(df)


real target = np.array(real_target)


target_predict


real_target
