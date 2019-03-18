# --------------
# Importing header files
import numpy as np

# Path of the file has been stored in variable called 'path'

#New record
new_record=[[50,  9,  4,  1,  0,  0, 40,  0]]

#Code starts here
data=np.genfromtxt(path,delimiter=",", skip_header=1)
census=np.concatenate((np.array(new_record),data))


# --------------
#Code starts here
age=census[:,0]
print(age)

max_age=age.max()
print(max_age)
min_age=age.min()
print(min_age)
age_mean=age.mean()
print(age_mean)
age_std=np.std(age)
print(age_std)


# --------------
#Code starts here
race_0=census[np.where(census[:,2]==0)]
race_1=census[np.where(census[:,2]==1)]
race_2=census[np.where(census[:,2]==2)]
race_3=census[np.where(census[:,2]==3)]
race_4=census[np.where(census[:,2]==4)]

len_0=len(race_0)
len_1=len(race_1)
len_2=len(race_2)
len_3=len(race_3)
len_4=len(race_4)

mini=min(len_0,len_1,len_2,len_3,len_4)

if(mini==len_0):
    minority_race=0
elif (mini==len_1):
    minority_race=1
elif (mini==len_2):
    minority_race=2
elif (mini==len_3):
    minority_race=3
elif (mini==len_4):
    minority_race=4
print(minority_race)











# --------------
#Code starts here
senior_citizens=census[census[:,0]>60]
working_hours_sum=np.sum(senior_citizens[:,6])

senior_citizens_len=len(senior_citizens)
avg_working_hours=working_hours_sum/senior_citizens_len
print(avg_working_hours)


# --------------
#Code starts here
high=census[census[:,1]>10]
low=census[census[:,1]<=10]

avg_pay_high=np.mean(high[:,7])
avg_pay_low=np.mean(low[:,7])


