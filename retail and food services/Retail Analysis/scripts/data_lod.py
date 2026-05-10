import pandas as pd

# Step 1: Data Load
df = pd.read_csv('retail-analysis/data/retail.csv') 

# Check karo
print("✅ Data Loaded!")
print("Shape:", df.shape)
print("Columns:", df.columns.tolist())
print(df.head())