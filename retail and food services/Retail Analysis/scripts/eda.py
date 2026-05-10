import pandas as pd

# ── Load Clean Data ────────────────────────────────────
base = r'C:\Users\KRISH\OneDrive\Music\Desktop\retail and food services\retail-analysis'

df = pd.read_csv(base + r'\data\retail_clean.csv', parse_dates=['month'])

print("=== Shape ===")
print(df.shape)

print("\n=== Data Types ===")
print(df.dtypes)

print("\n=== Summary Statistics ===")
print(df.describe())

print("\n=== Top 10 Businesses by Value ===")
print(df.groupby('kind_of_business')['value'].sum().nlargest(10))

print("\n=== Month-wise Total Value ===")
print(df.groupby('month')['value'].sum())

print("\n=== Yearly Total Value ===")
df['year'] = df['month'].dt.year
print(df.groupby('year')['value'].sum())

print("\n=== Unique NAICS Codes ===")
print(df['naics_code'].nunique())

print("\n=== Unique Businesses ===")
print(df['kind_of_business'].nunique())

print("\n=== Correlation ===")
print(df.corr(numeric_only=True))