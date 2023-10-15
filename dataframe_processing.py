import numpy as np
import matplotlib
import seaborn
import pandas as pd

df = pd.read_csv("C:\\Users\\Owner\\Desktop\\Coding\\Xtern Application\\AI Prompt\\data.csv")

# first five rows
print(df.head())

# summary of data stats (size, mean, std, min, med, max, Q1, Q3)
print(df.describe())

# the number of null values in each column
print(df.isnull().sum())

# drops missing values
df.dropna(inplace=True) 

# Fill with a constant
df.fillna(value=0, inplace=True) 

# Fill with mean, median, or mode
df['column_name'].fillna(df['column_name'].mean(), inplace=True)

# converts a column to specified type (int)
df['column_name'] = df['column_name'].astype('int')

# apply functions to a column
df['new_column'] = df['column_name'].apply(lambda x: x*2)

# min-max normalization
df['normalized_column'] = (df['column_name'] - df['column_name'].min()) / (df['column_name'].max() - df['column_name'].min())

""" ENCODING CATEGORICAL DATA """

# one-hot encoding
df = pd.get_dummies(df, columns=['categorical_column'])

# label encoding
from sklearn.preprocessing import LabelEncoder

le = LabelEncoder()
df['encoded_column'] = le.fit_transform(df['categorical_column'])

""" FILTERING DATA """

# Filter rows based on condition
min = 5
filtered_df = df[df['column_name'] > min]

# Select specific columns
selected_df = df[['column1', 'column2']]

""" AGGREGATING DATA """

# Group by a column and calculate aggregates
grouped = df.groupby('column_name').agg({'another_column': 'mean'})

""" MERGING, JOINING, AND CONCATENATING """

# concatenate dataframes
df_new = pd.concat([df1, df2])

# merge dataframes
merged_df = pd.merge(df1, df2, on='common_column')

""" HANDLING TIME SERIES DATA """

# Convert a column to datetime format
df['date_column'] = pd.to_datetime(df['date_column'])

# Extract year, month, day, etc.
df['year'] = df['date_column'].dt.year

""" SAVING THE PROCESSED DATA """

df.to_csv('processed_data.csv', index=False)



