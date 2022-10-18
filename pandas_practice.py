import csv

import pandas as pd

# technologies = {
#     'Courses': ["Spark", "PySpark", "Python"],
#     'Fee': [22000, 25000, 24000],
#     'Duration': ['30day', None, '55days'],
#     'Discount': [1000, 2300, 1000]
#           }
# df = pd.DataFrame(technologies)
# df.to_csv('numbers.csv', index=False, sep="|")


# info =  {'X':[78,85,96,80,86], 'Y':[84,94,89,83,86],'Z':[86,97,96,72,83]}
# df = pd.DataFrame(info)
# print(df)
# df.to_csv('numbers.csv')

import numpy as np

# exam_data = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
# 'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
# 'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
# 'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}
# labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
#
# df = pd.DataFrame(exam_data, index=labels)
# print("Summary of the basic information about this DataFrame and its data: ")
# print(df.info()) #vad toate informatiile despre acest dataframe

# print(df.iloc[0:3]) #vad primele 3 randuri din dataframe
# print(df[['name', 'score']]) #vad doar informatiile pentru coloanele name, score
# print(df.iloc[[1, 3, 5, 6], ['name']]) # se ia in calcul in functie de index, primele [] ce randuri vreau, a doua [] ce coloane vreau
# print(df[df['attempts']>2]) #conditie: sa se afiseze info pt attempts>2
# print('Numbers of columns: ', len(df.columns)) #nr de coloane
# print('Number of rows:', len(df)) #nr de randuri
# print(df[df['score'].isnull()]) #returneaza missing data -> NaN
# print(df[df['score'].between(15,20)])
# print(df[(df['attempts']<2) & (df['score']>15)]) #conditii pe coloane diferite
# df.loc['d', 'score'] = 11.5
# print(df)
# print(df['attempts'].sum())
# print(df['score'].mean())
# k = {'name': "Suresh", 'score': 15.5, 'attempts': 1, 'qualify': "yes"}
# df.loc['k'] = ['Suresh', 'yes', 1, 15.5]
# # print(df)
# df = df.drop('k')
# print(df)

exam_data = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

df = pd.DataFrame(exam_data, index=labels)
# print(df)
# print(df.info()) # summary of the basic information about a specified DataFrame
# print(df[:3]) #Write a Pandas program to get the first 3 rows
# print(df.iloc[:3]) #Write a Pandas program to get the first 3 rows
# print(df[['name', 'score']]) #program to select the 'name' and 'score' columns
# print(df.iloc[[1,3,5,6], [1,3]])#to select the specified columns and rows from a given data frame. Select 'name' and 'score' columns in rows 1, 3, 5, 6
# print(df[df['attempts']>2])#Number of attempts in the examination is greater than 2
# print(len(df.columns))#to count the number of columns
# print(len(df))#to count the number of rows
# print(df[df['score'].isnull()]) #to select the rows where the score is missing, i.e. is NaN
# print(df[df['score'].between(15, 20)]) #select the rows the score is between 15 and 20 (inclusive)
# print(df[(df['score'] > 15) & (df['attempts']<2)]) #to select the rows where number of attempts in the examination is less than 2 and score greater than 15.
# df.loc['d','score'] = 11.5 #change the score in row 'd' to 11.5
# print(df)
# print(sum(df['attempts'])) #calculate the sum of the examination attempts
# print(df['score'].mean()) #calculate the mean score for each different student
# to append a new row 'k' to data frame with given values for each column
# df.loc['k'] = ['Suresh', 15.5, 1, 'yes']
# print(df)
# df = df.drop('k')# Now delete the new row
# print(df)# return the original DataFrame
# df.sort_values(by=['name', 'score'], ascending=[False, True]) #Sort the data frame first by 'name' in descending order, then by 'score' in ascending order
# print(df)




