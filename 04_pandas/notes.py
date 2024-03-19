import sys
import pandas as pd
import numpy as np
import os

#Check syntax
pd.Series([1,-1,1,-1])
pd.Series({'aa':1, 'aaa':'b', 'aaaa':'g'})
pd.DataFrame({'var':[1,2,3], 'column2':[0,0,0]})
pd.DataFrame([{'var':1,'column2':0},{'var':2,'column2':0},{'var':3,'column2':0}])

#DATA CSV
df = pd.read_csv(r'04_pandas\auxiliary\data_2017_zs.csv', sep = ';', on_bad_lines= 'skip')
df.head(10)
df = df.rename(columns = {
    'cislo_dot' : 'number',
    'kod_predm' : 'course_code',
    'nazev_predm' : 'course_title',
    'prednasejici' : 'teachers',
    'cvicici' : 'seminar_leaders',
    't1': 'c_value',
    't2': 'c_improve', 
    'katedra_code' : 'department_code'
})
df.set_index('number', inplace = True)
df.describe()
df['course_title'] #series
df[['course_title']] #dataframe because here we can select multiple columns
df[['course_title','teachers']] #like this
df['tmp'] = '11/10' #add column
df.drop('tmp', axis = 1,  inplace = True) #axis = 0 removes rows and axis = 1 removes columns

print(df.loc[5:25:3,['department_code','teachers']])
df_ies = df.loc[df['department_code'] == 'ies']

import itertools
import random
def fourSum(nums, target):
    all_combinations = list(itertools.combinations(nums, 4))
    answer = []
    for i in all_combinations:
        i_sorted = sorted(i)
        if (sum(i_sorted) == target) and (i_sorted not in answer):
            answer.append(i_sorted)
    return(answer)

print(fourSum([-490,-481,-471,-467,-453,-450,-446,-440,-437,-424,-423,-391,-384,-373,-358,-332,-318,-314,-311,-309,-299,-279,-270,-257,-243,-208,-205,-171,-153,-147,-142,-138,-129,-99,-20,-19,17,30,44,82,86,93,122,125,138,139,158,169,175,181,199,200,203,203,205,225,248,272,277,306,334,335,337,338,342,344,359,396,403,405,412,434,437,439,440,441,443,446,446,457,465,468,473,496], 1896))
print(len([-490,-481,-471,-467,-453,-450,-446,-440,-437,-424,-423,-391,-384,-373,-358,-332,-318,-314,-311,-309,-299,-279,-270,-257,-243,-208,-205,-171,-153,-147,-142,-138,-129,-99,-20,-19,17,30,44,82,86,93,122,125,138,139,158,169,175,181,199,200,203,203,205,225,248,272,277,306,334,335,337,338,342,344,359,396,403,405,412,434,437,439,440,441,443,446,446,457,465,468,473,496]))
