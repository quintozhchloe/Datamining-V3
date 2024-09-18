# -*- coding: utf-8 -*-
"""
Created on Wed May  1 15:26:43 2024

@author: Chloe huang
"""
# 02 data understanding
import pandas as pd
import numpy as np

# Load datasets
poverty_data = pd.read_csv('multidimensional_poverty.csv')
income_data = pd.read_csv('Inequality in Income.csv')
gender_ineq_data = pd.read_csv('gender_inequality.csv')
 
p_df =poverty_data
print(p_df)
p_df.head()
p_df.shape
p_df.info()
p_df.dtypes


i_df =income_data
print(i_df)
i_df.head()
i_df.shape
i_df.info()
i_df.dtypes

g_df =gender_ineq_data
print(g_df)
g_df.head()
g_df.shape
g_df.info()
g_df.dtypes


# Explore Data

#poverty
p_df =poverty_data
p_df.info()
p_df.describe()
p_df_desc=p_df.describe()


total_nulls_p = p_df.isna().sum().sum()
print(total_nulls_p)

round(p_df_desc,2)
round(p_df_desc.transpose(),2)

p_df[['Health Deprivation','Population Below National Poverty Line','Education Deprivation','Living Standards','Population Below National Poverty Line','Population Below $1.25 per Day']].describe()
p_df['Country'].value_counts()

#3.5 formatting
#convert object to float64

p_df['Population Below National Poverty Line'] = pd.to_numeric(p_df['Population Below National Poverty Line'], errors='coerce')
p_df['Population Below $1.25 per Day'] = pd.to_numeric(p_df['Population Below $1.25 per Day'], errors='coerce')
p_df.head()


numeric_df = p_df.select_dtypes(include=[np.number])
numeric_df.corr()

p_df_corr=round(numeric_df.corr(),2)

# correct the abnormol value

p_df_clean = numeric_df.replace("..", np.nan)
for col in p_df_clean.columns:
    p_df_clean[col] = pd.to_numeric(p_df_clean[col], errors='coerce')

# Calculate the median for each column, ignoring NaN
medians = p_df_clean.median()

# Replace NaN values with the corresponding median values
p_df_clean = p_df_clean.fillna(medians)



#analysis their corr
p_df_clean[['Health Deprivation','Intensity of Deprivation','Population Below National Poverty Line','Education Deprivation','Living Standards','Population Below $1.25 per Day']].corr()

p_df_clean[['Health Deprivation','Population Below National Poverty Line','Education Deprivation','Living Standards']].groupby('Population Below National Poverty Line').agg('mean')

p_df_clean[['Health Deprivation','Population Below $1.25 per Day','Education Deprivation','Living Standards']].groupby('Population Below $1.25 per Day').describe()




#income
#null sum
total_nulls_i = i_df.isna().sum().sum()
print(total_nulls_i)

i_df.info()
i_df.describe()
i_df_desc=i_df.describe()
round(i_df_desc,2)
round(i_df_desc.transpose(),2)


# num cols
numeric_df_i = i_df.select_dtypes(include=[np.number])

# Replace NaN values with the corresponding median values
medians_i = numeric_df_i.median()
i_df_clean = numeric_df_i.fillna(medians_i)



i_df_clean[['HDI Rank (2021)','Inequality in income (2010)','Inequality in income (2011)','Inequality in income (2021)']].describe()

i_df_corr=round(numeric_df_i.corr(),2)

i_df[['HDI Rank (2021)','Inequality in income (2010)','Inequality in income (2011)','Inequality in income (2021)']].corr()


#gender

g_df.info()
g_df.describe()
g_df_desc=g_df.describe()


round(g_df_desc,2)
round(g_df_desc.transpose(),2)
#null sum
total_nulls_g = g_df.isna().sum().sum()
print(total_nulls_g)


#3.5
# convert object to float64
for col in g_df.columns:
    # Check if the column is of object type and is not 'country'
    if g_df[col].dtype == 'object' and col != 'Country':
       
        g_df[col] = pd.to_numeric(g_df[col], errors='coerce')

# num cols
numeric_df_g = g_df.select_dtypes(include=[np.number])



# Replace NaN values with the corresponding median values
medians_g = numeric_df_g.median()
g_df_clean = numeric_df_g.fillna(medians_g)
g_df_clean.corr()


g_df_clean[['Gender Inequality Index (GII)','Maternal Mortality Ratio','Adolescent Birth Rate','Percent Representation in Parliament','Population with Secondary Education (Female)','Population with Secondary Education (Male)','Labour Force Participation Rate (Female)','Labour Force Participation Rate (Male)']].describe()


g_df_corr=round(g_df_clean.corr(),2)

g_df_clean[['Gender Inequality Index (GII)','Maternal Mortality Ratio','Adolescent Birth Rate','Percent Representation in Parliament','Population with Secondary Education (Female)','Population with Secondary Education (Male)','Labour Force Participation Rate (Female)','Labour Force Participation Rate (Male)']].describe().corr()

g_df_clean[['Gender Inequality Index (GII)','Maternal Mortality Ratio','Adolescent Birth Rate','Percent Representation in Parliament','Population with Secondary Education (Female)','Population with Secondary Education (Male)','Labour Force Participation Rate (Female)','Labour Force Participation Rate (Male)']].describe().groupby('Gender Inequality Index (GII)').agg('mean')

g_df_clean[['Gender Inequality Index (GII)','Maternal Mortality Ratio','Adolescent Birth Rate','Percent Representation in Parliament','Population with Secondary Education (Female)','Population with Secondary Education (Male)','Labour Force Participation Rate (Female)','Labour Force Participation Rate (Male)']].describe().groupby('Gender Inequality Index (GII)').describe()

round(g_df_clean[['Gender Inequality Index (GII)','Maternal Mortality Ratio','Adolescent Birth Rate','Percent Representation in Parliament','Population with Secondary Education (Female)','Population with Secondary Education (Male)','Labour Force Participation Rate (Female)','Labour Force Participation Rate (Male)']].describe().groupby('Gender Inequality Index (GII)').
      describe().transpose(),2)





# Add Visualisations

p_df_clean[['Population Below National Poverty Line']].plot()
p_df_clean[['Population Below National Poverty Line']].plot().sample(n=100).plot()
p_df_clean[['Population Below National Poverty Line']].plot.hist()
p_df_clean[['Population Below National Poverty Line']].plot().density()
p_df_clean[['Population Below National Poverty Line']].plot().box()
p_df_clean[['Population Below National Poverty Line']].plot().bar()


p_df_clean[['Population Below National Poverty Line']].value_counts().plot.bar()



p_df_clean.plot.box(column='Population Below National Poverty Line',by='Education Deprivation')
p_df_clean.plot.box(column='Population Below National Poverty Line',by='Living Standards')
p_df_clean.plot.box(column='Population Below National Poverty Line',by='Health Deprivation')

p_df_clean.plot.scatter(x='Population Below National Poverty Line',y='Education Deprivation')
p_df_clean.plot.scatter(x='Population Below National Poverty Line',y='Health Deprivation')
p_df_clean.plot.scatter(x='Population Below National Poverty Line',y='Living Standards')


p_df_clean.sample(n=100).plot.scatter(x='Population Below National Poverty Line',y='Living Standards')



   



#3.1 filtering unnecessary cols



#poverty
# List of columns to keep
columns_to_keep_p =['Country', 'Education Deprivation', 'Health Deprivation', 'Living Standards', 'Population Below National Poverty Line', 'Population Below $1.25 per Day' ]  # Replace with actual column names

p_df_s = p_df[columns_to_keep_p]
p_df_s.to_csv('C:\\Users\\Administrator\\Desktop\\722 Data mining\\Assignment\\A1\\Iteration3\\Poverty_dataset_selected.csv', index=False)
p_df_s.head()

#income
selected_columns_i = ['Country', 'Human Development Groups', 'Inequality in income (2010)', 'Inequality in income (2011)', 'Inequality in income (2012)','Inequality in income (2013)','Inequality in income (2014)','Inequality in income (2015)','Inequality in income (2016)','Inequality in income (2017)','Inequality in income (2018)','Inequality in income (2019)','Inequality in income (2020)','Inequality in income (2021)']
i_df_s = i_df[selected_columns_i]
i_df_s.head()
i_df_s.to_csv('C:\\Users\\Administrator\\Desktop\\722 Data mining\\Assignment\\A1\\Iteration3\\Income_dataset_selected.csv', index=False)

#gender
selected_columns_g = ['Country', 'GII Rank', 'Gender Inequality Index (GII)', 'Population with Secondary Education (Female)', 'Population with Secondary Education (Male)']
g_df_s = g_df[selected_columns_g]
g_df_s.head()
g_df_s.to_csv('C:\\Users\\Administrator\\Desktop\\722 Data mining\\Assignment\\A1\\Iteration3\\Gender_dataset_selected.csv', index=False)





# 3.2 data cleaning
# empty values

p_data = pd.read_csv('Poverty_dataset_selected.csv')
i_data = pd.read_csv('Income_dataset_selected.csv')
g_ineq_data = pd.read_csv('Gender_dataset_selected.csv')
 


duplicate_rows_p = p_data.duplicated().sum()
duplicate_rows_i = i_df_s.duplicated().sum()
duplicate_rows_g = g_df_s.duplicated().sum()



#3.4 - merge data
#Integration must take place. This includes effectively merging data from various sources. 
#merge data

# Re-printing column names to verify
datasets = [p_data, i_data, g_ineq_data]
names = ["poverty_data", "income_data", "gender_ineq_data"]

merged_df = pd.merge(g_ineq_data, i_data, on='Country', how='outer')
merged_df = pd.merge(merged_df, p_data, on='Country', how='outer')

# Save the merged DataFrame to a new CSV file

merged_df.to_csv('C:\\Users\\Administrator\\Desktop\\722 Data mining\\Assignment\\A1\\Final dataset\\merged_dataset.csv', index=False)

# Optionally, display the first few rows of the merged dataset to confirm it looks correct
 
   
merged_df.head()
merged_df.shape
merged_df.info()
merged_df.dtypes


duplicate_rows = merged_df.duplicated().sum()

total_nulls = merged_df.isna().sum().sum()
# expect the rows with null in Population Below National Poverty Line & Population Below $1.25 per Day at the same time

df_cleaned = merged_df.dropna(subset=['Population Below National Poverty Line', 'Population Below $1.25 per Day'], how='all')

# Save the cleaned DataFrame back to a CSV file (optional)
df_cleaned.to_csv('C://Users//Administrator//Desktop//722 Data mining//Assignment//A1//Final dataset//Clean_dataset.csv', index=False)

# Print the first few rows of the cleaned DataFrame to verify that rows with missing values have been removed
print(df_cleaned.head())
df_cleaned.shape










#3.3 -Constructing the data.
#Data must be appropriately constructed through the creation of new features/variables, and/or data repositories/tables. 
import pandas as pd
import numpy as np

cd = pd.read_csv('Clean_dataset.csv')
numeric_cd=cd.select_dtypes(include=[np.number])


# Replace NaN values with the corresponding median values
medians_i = numeric_cd.median()
cd = numeric_cd.fillna(medians_i)

total_nulls_clean = cd.isna().sum().sum()




#p
cd['Poverty Severity'] = cd['Education Deprivation'] * cd['Health Deprivation'] * cd['Living Standards']


#i
columns_of_interest = ['Inequality in income (2010)', 'Inequality in income (2011)', 'Inequality in income (2012)',
                       'Inequality in income (2013)','Inequality in income (2014)','Inequality in income (2015)',
                       'Inequality in income (2016)','Inequality in income (2017)','Inequality in income (2018)',
                       'Inequality in income (2019)','Inequality in income (2020)','Inequality in income (2021)']  # Adjust column names as needed
cd['Average_income_inequality'] = cd[columns_of_interest].mean(axis=1)
cd.head()
cd.shape
cd.dtypes

cd = cd.drop(columns=['Inequality in income (2010)', 'Inequality in income (2011)', 'Inequality in income (2012)',
                       'Inequality in income (2013)','Inequality in income (2014)','Inequality in income (2015)',
                       'Inequality in income (2016)','Inequality in income (2017)','Inequality in income (2018)',
                       'Inequality in income (2019)','Inequality in income (2020)','Inequality in income (2021)'])  

df= pd.read_csv('Clean_dataset.csv')
string_df=df.select_dtypes(exclude=[np.number])


cd= pd.concat([string_df,cd], axis=1)
cd['Human Development Groups'].fillna(value='Medium', inplace=True)


cd.to_csv('C://Users//Administrator//Desktop//722 Data mining//Assignment//A1//Final dataset//Clean_dataset_New.csv', index=False)


