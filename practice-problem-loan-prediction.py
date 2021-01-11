import pandas as pd
import numpy as np

train_ctrUa4K=['Loan_ID', 'Gender', 'Married', 'Dependents', 'Education',
       'Self_Employed', 'ApplicantIncome', 'CoapplicantIncome', 'LoanAmount',
       'Loan_Amount_Term', 'Credit_History', 'Property_Area', 'Loan_Status']


columns=["Identifier","Edition_Statement","Place_of_Publication","Date_of_Publication","Publisher","Title","Author","Contributors","Corporate_Author","Corporate_Contributors","Former_owner","Engraver","Issuance_type","Flickr_URL,Shelfmarks"]
train_ctrUa4K = pd.read_csv('train_ctrUa4K.csv',sep=',')


#Education
train_ctrUa4K = train_ctrUa4K.dropna()
train_ctrUa4K.loc[train_ctrUa4K['Education'] == 'Graduate', 'Education'] = int(1)
train_ctrUa4K.loc[train_ctrUa4K['Education'] == 'Not Graduate', 'Education'] = int(2)

train_ctrUa4K['Education'] = train_ctrUa4K.Education.astype(float)
Education=train_ctrUa4K['Education'].unique()



#Gender
train_ctrUa4K.loc[train_ctrUa4K['Gender'] == 'Male', 'Gender'] = int(1)
train_ctrUa4K.loc[train_ctrUa4K['Gender'] == 'Female', 'Gender'] = int(2)
train_ctrUa4K['Gender'] = train_ctrUa4K.Education.astype(float)
Gender=train_ctrUa4K['Gender'].unique()






#Married
train_ctrUa4K.loc[train_ctrUa4K['Married'] == 'Yes', 'Married'] = int(1)
train_ctrUa4K.loc[train_ctrUa4K['Married'] == 'No', 'Married'] = int(2)
train_ctrUa4K['Married'] = train_ctrUa4K.Married.astype(float)
Married=train_ctrUa4K['Married'].unique()



#Dependents
train_ctrUa4K.loc[train_ctrUa4K['Dependents'] == '0', 'Dependents'] = int(0)
train_ctrUa4K.loc[train_ctrUa4K['Dependents'] == '1', 'Dependents'] = int(1)
train_ctrUa4K.loc[train_ctrUa4K['Dependents'] == '2', 'Dependents'] = int(2)
train_ctrUa4K.loc[train_ctrUa4K['Dependents'] == '3+', 'Dependents'] = int(3)

train_ctrUa4K['Dependents'] = train_ctrUa4K.Dependents.astype(int)
Dependents=train_ctrUa4K['Dependents'].unique()




#Self_Employed
train_ctrUa4K.loc[train_ctrUa4K['Self_Employed'] == 'No', 'Self_Employed'] = int(0)
train_ctrUa4K.loc[train_ctrUa4K['Self_Employed'] == 'Yes', 'Self_Employed'] = int(1)

train_ctrUa4K['Self_Employed'] = train_ctrUa4K.Self_Employed.astype(int)
Self_Employed=train_ctrUa4K['Self_Employed'].unique()


  

#Property_Area
train_ctrUa4K.loc[train_ctrUa4K['Property_Area'] == 'Rural', 'Property_Area'] = int(0)
train_ctrUa4K.loc[train_ctrUa4K['Property_Area'] == 'Urban', 'Property_Area'] = int(1)
train_ctrUa4K.loc[train_ctrUa4K['Property_Area'] == 'Semiurban', 'Property_Area'] = int(2)

train_ctrUa4K['Property_Area'] = train_ctrUa4K.Property_Area.astype(int)
Property_Area=train_ctrUa4K['Property_Area'].unique()




#Loan_Status
train_ctrUa4K.loc[train_ctrUa4K['Loan_Status'] == 'N', 'Loan_Status'] = int(0)
train_ctrUa4K.loc[train_ctrUa4K['Loan_Status'] == 'Y', 'Loan_Status'] = int(1)

train_ctrUa4K['Loan_Status'] = train_ctrUa4K.Loan_Status.astype(int)
Loan_Status=train_ctrUa4K['Loan_Status'].unique()


'''
'''




test_lAUu6dG = pd.read_csv('test_lAUu6dG.csv',sep=',')
test_lAUu6dG = test_lAUu6dG.dropna()


#Education
test_lAUu6dG=test_lAUu6dG.dropna()
test_lAUu6dG.loc[test_lAUu6dG['Education'] == 'Graduate', 'Education'] = int(1)
test_lAUu6dG.loc[test_lAUu6dG['Education'] == 'Not Graduate', 'Education'] = int(2)

test_lAUu6dG['Education'] = test_lAUu6dG.Education.astype(float)
Education=test_lAUu6dG['Education'].unique()



#Gender
test_lAUu6dG.loc[test_lAUu6dG['Gender'] == 'Male', 'Gender'] = int(1)
test_lAUu6dG.loc[test_lAUu6dG['Gender'] == 'Female', 'Gender'] = int(2)
test_lAUu6dG['Gender'] = test_lAUu6dG.Education.astype(float)
Gender=test_lAUu6dG['Gender'].unique()






#Married
test_lAUu6dG.loc[test_lAUu6dG['Married'] == 'Yes', 'Married'] = int(1)
test_lAUu6dG.loc[test_lAUu6dG['Married'] == 'No', 'Married'] = int(2)
test_lAUu6dG['Married'] = test_lAUu6dG.Married.astype(float)
Married=test_lAUu6dG['Married'].unique()



#Dependents
test_lAUu6dG.loc[test_lAUu6dG['Dependents'] == '0', 'Dependents'] = int(0)
test_lAUu6dG.loc[test_lAUu6dG['Dependents'] == '1', 'Dependents'] = int(1)
test_lAUu6dG.loc[test_lAUu6dG['Dependents'] == '2', 'Dependents'] = int(2)
test_lAUu6dG.loc[test_lAUu6dG['Dependents'] == '3+', 'Dependents'] = int(3)

test_lAUu6dG['Dependents'] = test_lAUu6dG.Dependents.astype(int)
Dependents=train_ctrUa4K['Dependents'].unique()




#Self_Employed
test_lAUu6dG.loc[test_lAUu6dG['Self_Employed'] == 'No', 'Self_Employed'] = int(0)
test_lAUu6dG.loc[test_lAUu6dG['Self_Employed'] == 'Yes', 'Self_Employed'] = int(1)

test_lAUu6dG['Self_Employed'] = test_lAUu6dG.Self_Employed.astype(int)
Self_Employed=test_lAUu6dG['Self_Employed'].unique()


  

#Property_Area
test_lAUu6dG.loc[test_lAUu6dG['Property_Area'] == 'Rural', 'Property_Area'] = int(0)
test_lAUu6dG.loc[test_lAUu6dG['Property_Area'] == 'Urban', 'Property_Area'] = int(1)
test_lAUu6dG.loc[test_lAUu6dG['Property_Area'] == 'Semiurban', 'Property_Area'] = int(2)

test_lAUu6dG['Property_Area'] = test_lAUu6dG.Property_Area.astype(int)
Property_Area=test_lAUu6dG['Property_Area'].unique()













'''
'''





sample_submission_49d68Cx = pd.read_csv('sample_submission_49d68Cx.csv',sep=',')

#Loan_Status
sample_submission_49d68Cx.loc[sample_submission_49d68Cx['Loan_Status'] == 'N', 'Loan_Status'] = int(0)
sample_submission_49d68Cx.loc[sample_submission_49d68Cx['Loan_Status'] == 'Y', 'Loan_Status'] = int(1)

sample_submission_49d68Cx['Loan_Status'] = sample_submission_49d68Cx.Loan_Status.astype(int)
Loan_Status=sample_submission_49d68Cx['Loan_Status'].unique()


'''
split data
'''
x_train=train_ctrUa4K.drop(['Loan_Status'],axis=1)
x_train=x_train.drop(['Loan_ID'],axis=1)
print(x_train.columns)

y_train=train_ctrUa4K['Loan_Status']
#print(y_train)

#test_lAUu6dG
x_test=test_lAUu6dG.drop(['Loan_ID'],axis=1)
print(x_test.columns)


'''
Logistic ragression
'''


from sklearn.linear_model import LogisticRegression


logreg = LogisticRegression()

logreg.fit(x_train,y_train)



#predict

new_obs=x_test
y_pred=logreg.predict(new_obs)
print(y_pred)

ypv=[]
for i in y_pred:
	if (i==0):
		ypv.append("N")
	if (i==1):
		ypv.append("Y")

print(ypv)
'''yid=[train_ctrUa4K['Loan_ID']]
print(yid)
'''
yid=[]
for i in test_lAUu6dG['Loan_ID']:
	yid.append(i)

print(yid)




d = {'Loan_ID':yid,'Loan_Status':ypv}
df = pd.DataFrame(d)	
print(df)

df.to_csv (r'C:\Users\Bachi\Desktop\practice-problem-loan-prediction\df.csv', index = False, header=True)

print (df)	
