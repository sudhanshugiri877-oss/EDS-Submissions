import pandas as pd
from itertools import combinations
from collections import Counter

# Prompt user to input the file name
file_name = input()

# Read data from the specified CSV file
df = pd.read_csv(file_name)

# write the code
grouped=df.groupby("Date")["Product"].apply(list)
product_pair=[]
for products in grouped:
	if len(products)>1:
		product_pair.extend(combinations(sorted(products),2))
pair_counts=Counter(product_pair)

if pair_counts:
	max_count=max(pair_counts.values())
	most_common_pairs=[pair for pair,count in pair_counts.items() if count == max_count]
	for pair in sorted(most_common_pairs):
		print(f"{pair[0]} and {pair[1]}: {max_count} times")