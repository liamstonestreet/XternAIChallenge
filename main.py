import numpy as np
import matplotlib
from matplotlib import pyplot as plt
import seaborn
import pandas as pd

df = pd.read_csv("C:\\Users\\Owner\\Desktop\\Coding\\Xtern Application\\AI Prompt\\data.csv")

# first five rows
print(df.head())

# summary of data stats (size, mean, std, min, med, max, Q1, Q3)
#print(df.describe())

# prints value at row 0 and column 'Major'
#print(df.at[0, 'Major'])

# reformats the 'year' column so that it's just a numerical value
df['Year'] = df['Year'].apply(lambda x: x.lstrip("Year "))   

print(df.head())