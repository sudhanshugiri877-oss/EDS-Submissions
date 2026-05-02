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

# Write your code here for Bar Plot for Survival by Gender
# 1. Create a cross-tabulation (contingency table) of Sex and Survived
# This organizes the counts so 'Sex' is the index and 'Survived' are the columns
survival_by_gender = pd.crosstab(data['Sex'], data['Survived'])

# 2. Plot the data
# kind='bar' creates the bars
# stacked=True places 'Survived' (1) on top of 'Not Survived' (0)
survival_by_gender.plot(kind='bar', stacked=True)

# 3. Apply exact formatting to match the "Expected output"
plt.title('Survival by Gender')
plt.xlabel('Gender')
plt.ylabel('Count')

# 4. Set the legend to match the labels in the expected image
plt.legend(['Not Survived', 'Survived'])

plt.show()