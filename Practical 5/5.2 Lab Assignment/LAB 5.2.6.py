import pandas as pd
import matplotlib.pyplot as plt

# Load the Titanic dataset
data = pd.read_csv('Titanic-Dataset.csv')

# Data Cleaning
data['Age'].fillna(data['Age'].median(), inplace=True)
data['Embarked'].fillna(data['Embarked'].mode()[0], inplace=True)
data.drop('Cabin', axis=1, inplace=True)

# Convert categorical features to numeric
data['Sex'] = data['Sex'].map({'male': 0, 'female': 1})
data = pd.get_dummies(data, columns=['Embarked'], drop_first=True)

# --- Write your code here for Bar Plot for Survival by Embarked ---

# 1. Use the 'Embarked_Q' column (created by get_dummies) to cross-tabulate with Survived
grouped = pd.crosstab(data['Embarked_Q'], data['Survived'])

# 2. Plot as a stacked bar chart
grouped.plot(kind='bar', stacked=True)

# 3. Add exact titles and labels as per instructions
plt.title('Survival by Embarked')
plt.xlabel('Embarked')
plt.ylabel('Count')

# 4. Include the legend with specific labels
plt.legend(['Not Survived', 'Survived'])

plt.show()