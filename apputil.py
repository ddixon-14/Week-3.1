import seaborn as sns
import pandas as pd
import numpy as np


"""Fib(n) returns the n'th number of the Fibonacci series"""
def fib(n):
    if n == 0: #base case
        return 0
    elif n == 1: #base case
        return 1
    else:
        return fib(n-1) + fib(n-2) #recursive case
    
print(fib(10)) 

"""to_binary(n) converts an integer into its binary representation"""
def to_binary(n):
    if n == 0:
        return "0"
    elif n == 1:
        return "1"
    else:
        return to_binary(n // 2) + str(n % 2)
print(to_binary(10))

"""task_i() functions complete the following tasks:
1. Return a list of all column names sorted such that the first column 
has the least missing values and the last column has the most 

2. Return a df with two columns year and total entries 

3. Returna series with index:gender and values: average age

4. Return a list of the 5 most common professions in order of prevalence"""



url = 'https://github.com/melaniewalsh/Intro-Cultural-Analytics/raw/master/book/data/bellevue_almshouse_modified.csv'

# df_bellevue = pd.read_csv(url)
# df_bellevue = pd.read_csv('./data/.../mydata.csv')  # you can also reference locally stored data

# Pt.1 return sorted column names 
# df_bellevue.columns.sort()

# Pt. 2 return df w/two columns year and totaly admissions 
# df_admissions_per_year = df_bellevue[['year', 'total_admissions']]

# pt. 3 return a series with index:gender and values: avg. age per indexed gender
# df_avg_age = df_bellevue.groupby('gender')['age'].mean()
# # found out groupby here isn't too different from r it seems 

# pt. 4 return a list of the 5 most common professions in order of prevalence 
# df_common_professions = df_bellevue['profession'].value_counts().head(5).index.tolist()
# captures professions as a series, counts values, takes top 5 (head), converts to list