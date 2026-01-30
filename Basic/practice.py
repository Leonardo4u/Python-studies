import pandas as pd

df = pd.read_csv('Basic/inventory.csv')

inventory = df['product_name'].tolist()

inventory.remove("Cheesy Chompers")
print(inventory)
