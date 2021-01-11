import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

#data=pd.read_csv('HeightsWeights.xlsx', index_col=0)

data=pd.read_excel('HeightsWeights.xlsx', index_col=0)  
#print(data.head(20))
data=data.iloc[3:]

#print(data.head(20))



new_header = data.iloc[0] #grab the first row for the header
data = data[1:] #take the data less the header row
data.columns = new_header #set the header row as the df header
#print(data.head(20))



#print(data.rename(columns={'Height': 'Height', 'Weight': 'Weight'}))
data.columns =['Height', 'Weight'] 
#print(data)


#predict the height

from sklearn.model_selection import train_test_split

#print(data.columns)

label=data[['Weight']]
label['Weight'] = label['Weight'].astype(float)
print("label:\n",label)


features=data[['Height']]
features['Height'] = features['Height'].astype(float)
print("features:\n",features)

x_train,x_test,y_train,y_test=train_test_split(features,label,test_size=0.2)

'''
print("x_train:\n",x_train)
print("x_test:\n",x_test)
print("y_train:\n",y_train)
print("y_test:\n",y_test)
'''

#LinearRegression

model = LinearRegression()

model.fit(x_train, y_train)
#model = LinearRegression().fit(x, y)

print(model)







