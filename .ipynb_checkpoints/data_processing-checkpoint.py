import numpy as np
from matplotlib import pyplot as plt
import seaborn
import pandas as pd

df = pd.read_csv("C:\\Users\\Owner\\Desktop\\Coding\\Xtern Application\\AI Prompt\\XternAIChallenge\\data.csv")

# plotting bar graph for class frequencies
course_counts = df['Major'].value_counts()
x = list(course_counts.keys())
y = list(course_counts.array)
#df['new_column'] = df['column_name'].apply(lambda x: x*2)

plt.bar(x, y, width=0.4)
plt.xticks(rotation=90)
plt.xlabel("Course")
plt.ylabel("Frequency")
plt.title("Course Sizes (# of people in each course)")
plt.show()
