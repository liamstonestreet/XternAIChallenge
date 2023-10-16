import numpy as np
from matplotlib import pyplot as plt
import seaborn as sns
import pandas as pd

df = pd.read_csv("C:\\Users\\Owner\\Desktop\\Coding\\Xtern Application\\AI Prompt\\XternAIChallenge\\data.csv") # the given dataset (csv format)

# plotting bar graph for class frequencies (sorted)
course_counts = df['Major'].value_counts()
x = list(course_counts.keys())
y = list(course_counts.array)

# Distribution of Majors
plt.bar(x, y)
plt.xticks(rotation=90)
plt.xlabel("Course")
plt.ylabel("Frequency")
plt.title("Course Sizes (# of people in each course)")
plt.show()

# Number of orders taken (by University)
plt.figure(figsize=(10, 6))
sns.countplot(data=df, y='University', hue='Order')
plt.title('Popular Orders by University')
plt.legend(loc='lower right')
plt.show()

# Number of orders taken (by Major)
plt.figure(figsize=(10, 6))
sns.countplot(data=df, y='Major', hue='Order')
plt.title('Popular Orders by Major')
plt.legend(loc='lower right')
plt.show()

# Average Time that orders are taken (by Major)
plt.figure(figsize=(10, 6))
plt.xticks(rotation=90)
sns.barplot(data=df, x='Major', y='Time')
plt.title('Average Time by Major')
plt.show()

# Distribution of Orders (by Students' Year -> Freshman - 1, Sophomore - 2, Junior - 3, Senior - 4)
plt.figure(figsize=(10, 6))
sns.countplot(data=df, x='Year')
plt.title('Distribution of Students Across Years')
plt.show()

