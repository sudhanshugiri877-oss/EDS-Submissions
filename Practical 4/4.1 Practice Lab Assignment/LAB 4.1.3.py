import pandas as pd

# Read the text file into a DataFrame
file = input()
data = pd.read_csv(file, sep="\s+", header=None, names=["Name", "Age", "Grade"])

print("First five rows:")
print(data.head())
avg_age=round(data["Age"].mean(),2)
print(f"Average age: {avg_age}")
print("Students with a grade up to B")
filtered_student = data[data["Grade"] <= "B"]
print(filtered_student)