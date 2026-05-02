import pandas as pd
import numpy as np

# Load the Titanic dataset
data = pd.read_csv('Titanic-Dataset.csv')
data['FamilySize'] = data['SibSp'] + data['Parch']

# 1. Create a new column ‘IsAlone' (1 if alone, 0 otherwise)
data['IsAlone'] = np.where(data['FamilySize' ]== 0, 1, 0)

# 2. Convert ‘Sex' to numeric (male: 0, female: 1)
data['Sex'] = data['Sex'].map({'male': 0, 'female': 1})

# 3. One-hot encode the ‘Embarked' column
data=pd.get_dummies(data,columns=['Embarked'],prefix='Embarked', drop_first=True)

# 4. Get the mean age of passengers
mean_age=data['Age'].mean()
print(mean_age)

# 5. Get the median fare of passengers
median_fare=data['Fare'].median()
print(median_fare)

# 6. Get the number of passengers by class
pc=data['Pclass'].value_counts()
print(pc)

# 7. Get the number of passengers by gender
pg=data['Sex'].value_counts()
print(pg)

# 8. Get the number of passengers by survival status
ps=data['Survived'].value_counts()
print(ps)

# 9. Calculate the survival rate
sr=data['Survived'].mean()
print(sr)

# 10. Calculate the survival rate by gender
srg=data.groupby('Sex')['Survived'].mean()
print(srg)