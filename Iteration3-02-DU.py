# -*- coding: utf-8 -*-
"""
Created on Wed May  1 11:24:02 2024

@author: Chloe huang
"""
# 02 data understanding
import pandas as pd
import numpy as np

# Load datasets
poverty_data = pd.read_csv('multidimensional_poverty.csv')
education_data = pd.read_csv('Inequality in Education.csv')
income_data = pd.read_csv('Inequality in Income.csv')
gender_ineq_data = pd.read_csv('gender_inequality.csv')
 
p_df =poverty_data
print(p_df)
p_df.head()
p_df.shape
p_df.info()

e_df =education_data
print(e_df)
e_df.head()
e_df.shape
e_df.info()

i_df =income_data
print(i_df)
i_df.head()
i_df.shape
i_df.info()

g_df =gender_ineq_data
print(g_df)
g_df.head()
g_df.shape
g_df.info()


# Explore Data


p_df =poverty_data
p_df.info()
p_df.describe()
p_df_desc=p_df.describe()


round(p_df_desc,2)
round(p_df_desc.transpose(),2)


p_df[['Health Deprivation','Population in Multidimensional Poverty','Education Deprivation','Living Standards']].describe()
p_df['Country'].value_counts()



numeric_df = p_df.select_dtypes(include=[np.number])
numeric_df.corr()


p_df_corr=round(numeric_df.corr(),2)

p_df[['Health Deprivation','Multidimensional Poverty Index (MPI, HDRO)','Education Deprivation','Living Standards']].corr()

p_df[['Health Deprivation','Multidimensional Poverty Index (MPI, HDRO)','Education Deprivation','Living Standards']].groupby('Multidimensional Poverty Index (MPI, HDRO)').agg('mean')

p_df[['Health Deprivation','Multidimensional Poverty Index (MPI, HDRO)','Education Deprivation','Living Standards']].groupby('Multidimensional Poverty Index (MPI, HDRO)').describe()


round(p_df[['Health Deprivation','Multidimensional Poverty Index (MPI, HDRO)','Education Deprivation','Living Standards']].groupby('Multidimensional Poverty Index (MPI, HDRO)').
      describe().transpose(),2)
#