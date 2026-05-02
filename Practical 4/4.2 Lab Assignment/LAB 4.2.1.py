import pandas as pd

# Prompt the user for the file name
file_name = input()

# Load the data
df = pd.read_csv(file_name)
df["Date"] = pd.to_datetime(df["Date"])
df["Month"] = df["Date"].dt.strftime("%Y-%m")
df["Total Sales"] = df["Quantity"] * df["Price"]
# Find the month with the highest total sales
sales_by_month = df.groupby("Month")["Total Sales"].sum()
best_month = sales_by_month.idxmax()
highest_sales = sales_by_month.max()

print(f"Best month: {best_month}")
print(f"Total sales: ${highest_sales:.2f}")
