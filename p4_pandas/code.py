# --------------
# Import packages
import numpy as np
import pandas as pd
from scipy.stats import mode 
 



# code starts here
bank=pd.read_csv(path)
categorical_var=bank.select_dtypes(include = 'object')
print(categorical_var)
numerical_var=bank.select_dtypes(include = 'number')
print(numerical_var)



# code ends here


# --------------
# code starts here
bank.drop(['Loan_ID'],inplace=True,axis=1)
print(bank.isnull().sum())
banks=bank
for column in banks.columns:
    bank_mode=banks[column].mode()[0]
    banks[column].fillna(bank_mode, inplace=True)
print(banks)


#code ends here


# --------------
# Code starts here




avg_loan_amount=pd.pivot_table(banks,index=['Gender', 'Married', 'Self_Employed'],values='LoanAmount',aggfunc='mean')



# code ends here



# --------------
# code starts here




l1=banks['Self_Employed']=='Yes'
l2=banks['Loan_Status']=='Y'
loan_approved_se=banks[l2 & l1].shape[0]


l3=banks['Self_Employed']=='No'
l4=banks['Loan_Status']=='Y'
loan_approved_nse=banks[l4 & l3].shape[0]

percentage_se=(loan_approved_se/614)*100
percentage_nse=(loan_approved_nse/614)*100

print(percentage_se)
print(percentage_nse)



# code ends here


# --------------
# code starts here



loan_term=banks['Loan_Amount_Term'].apply(lambda x : x/12)
big_loan_term=loan_term[loan_term>=25].count()
print(big_loan_term)





# code ends here


# --------------
# code starts here
loan_groupby=banks.groupby('Loan_Status')
loan_groupby=loan_groupby['ApplicantIncome', 'Credit_History']
mean_values=loan_groupby.mean()
print(mean_values)



# code ends here


