import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split 
from sklearn.linear_model import Linear Regression


iris = sns.load_dataset('iris')
iris = iris[['petal_length', 'petal_width']]


X = iris['petal_length']
y = iris['petal_width']


plt.scatter(x,y)
plt.xlabel("petal length") 
plt.ylabel("petal width")

﻿
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=32)


X_train = np.array(X_train).reshape(-1,1)
X_test np.array(X_test).reshape(-1,1)


lr = LinearRegression()
lr.fit(x_train, y_train)
y_pred = lr.predict(X_test)
plt.scatter(x_test, y_test, color="red") 
plt.scatter(x_test, y_pred, color="black")
