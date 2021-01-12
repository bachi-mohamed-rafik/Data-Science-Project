import pandas as pd


data=pd.read_csv('C:/Users/Bachi/Desktop/DS/capitalbikeshare/cap/2015Q1-capitalbikeshare-tripdata.csv',sep=',')

#print(data)

#print(data.columns)

#print(data.dtypes)

x=data.drop(['Start date'],axis=1)
x=x.drop(['End date'],axis=1)
x=x.drop(['Start station'],axis=1)
x=x.drop(['End station'],axis=1)
x=x.drop(['Bike number'],axis=1)
x=x.drop(['Member type'],axis=1)



data['Member type'] = data['Member type'].replace(['Casual'],0)
data['Member type'] = data['Member type'].replace(['Member'],1)

#print(x.columns)
#print(x.dtypes)

y=data['Member type']

#print(y)

import numpy as np
from sklearn.linear_model import LinearRegression





reg = LinearRegression().fit(x, y)

score=reg.score(x, y)
print(score)


#......................................................................................................................................................#



