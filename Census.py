import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

#2 Data Exploration:

train=pd.read_csv('C:/Users/Bachi/Desktop/DS/Census/train.csv',sep=',')


print(train.head(20))



# dataframe.size 
trsize = train.size 
print(trsize)

# dataframe.shape 
trshape = train.shape 
print(trshape)
  
# dataframe.ndim 
trdf_ndim = train.ndim
print(trdf_ndim)



test=pd.read_csv('C:/Users/Bachi/Desktop/DS/Census/test.csv',sep=',')
print(test.head(20))



# dataframe.size 
tssize = test.size 
print(tssize)
  
# dataframe.shape 
tsshape = test.shape 
print(tsshape)
  
# dataframe.ndim 
tsdf_ndim = test.ndim
print(tsdf_ndim)



#train data has 199523 rows & 41 columns. Test data has 99762 rows and 41 columns


#check first few rows of train & test

print(train[:5])
print(test[:5])


#check target variables

print(train['income_level'].unique())
print(test['income_level'].unique())


#check target variables

train.loc[train['income_level'] == -50000, 'income_level'] = 1
train.loc[train['income_level'] == +50000, 'income_level'] = 0

test.loc[test['income_level'] == '-50000', 'income_level'] = 1
test.loc[test['income_level'] == ' 50000+.', 'income_level'] = 0


#3. Data Cleaning

#check missing values in numerical data

print (train.isnull())
print (test.isnull())


#def ton(df):

#col=[]
col=train.columns
#print(col)

ctp=[]
ctp.append(train.dtypes)

#list if type object
lco=[]

for u in col:
	tpe=train.dtypes[u]
	if tpe=='object':
		lco.append(u)

for e in range(len(lco)):
	t=lco[e]
	tu=train[t].unique()
	j=0
	for i in tu:
		train.loc[train[t]==i,t]=j
		j=j+1
#	print(train[t])

#print(train.dtypes)
train[lco] = train[lco].apply(pd.to_numeric) 
#print(train.dtypes)
train.fillna(0)
train=train.replace(np.nan, 0)

x=train.drop(['income_level'], axis = 1) 
#print(x)
y=train['income_level']
#print(y)

#print(train.isnull().sum().sum())
model = LinearRegression()
model.fit(x, y)
#print(pd.isnull(train).sum() > 0)







#test data
#def ton(df):

#col=[]
col=test.columns
#print(col)

ctp=[]
ctp.append(test.dtypes)

#list if type object
lco=[]

for u in col:
	tpe=test.dtypes[u]
	if tpe=='object':
		lco.append(u)

for e in range(len(lco)):
	t=lco[e]
	tu=test[t].unique()
	j=0
	for i in tu:
		test.loc[test[t]==i,t]=j
		j=j+1
#	print(test[t])

#print(test.dtypes)
test[lco] = test[lco].apply(pd.to_numeric) 
#print(test.dtypes)
test.fillna(0)
test=test.replace(np.nan, 0)

xt=test.drop(['income_level'], axis = 1) 
#print(xt)
yt=test['income_level']
#print(yt)

#print(test.isnull().sum().sum())
#print(pd.isnull(test).sum() > 0)


y_pred = model.predict(xt)
print('predicted response:', y_pred, sep='\n')

