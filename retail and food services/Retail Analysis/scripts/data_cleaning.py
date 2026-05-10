import pandas as pd
import os

# ── Paths ──────────────────────────────────────────────
base = r'C:\Users\KRISH\OneDrive\Music\Desktop\retail and food services\retail-analysis'
raw_path   = os.path.join(base, 'data', 'retail.csv')        # ✅ retail.csv
clean_path = os.path.join(base, 'data', 'retail_clean.csv')

# ── Step 1: Load ───────────────────────────────────────
df = pd.read_csv(raw_path)
print("✅ Data Loaded!")
print("Shape:", df.shape)

# ── Step 2: Clean ──────────────────────────────────────
df.dropna(inplace=True)
df.drop_duplicates(inplace=True)
df['month'] = pd.to_datetime(df['month'])
df['naics_code'] = pd.to_numeric(df['naics_code'], errors='coerce')
df['value'] = pd.to_numeric(df['value'], errors='coerce')
df.dropna(inplace=True)

# ── Step 3: Check ──────────────────────────────────────
print("\n✅ Data Cleaned!")
print("Shape:", df.shape)
print("\nData Types:")
print(df.dtypes)
print("\nMissing Values:")
print(df.isnull().sum())

# ── Step 4: Save ───────────────────────────────────────
os.makedirs(os.path.join(base, 'data'), exist_ok=True)
df.to_csv(clean_path, index=False)
print("\n✅ Clean data saved → retail_clean.csv!")