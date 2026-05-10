import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# ── Load Clean Data ────────────────────────────────────
base = r'C:\Users\KRISH\OneDrive\Music\Desktop\retail and food services\retail-analysis'
df = pd.read_csv(base + r'\data\retail_clean.csv', parse_dates=['month'])
df['year'] = df['month'].dt.year

# Reports folder banana
os.makedirs(base + r'\reports', exist_ok=True)

# Style set karo
sns.set_theme(style='darkgrid')

# ── Plot 1: Yearly Trend ───────────────────────────────
yearly = df.groupby('year')['value'].sum().reset_index()

plt.figure(figsize=(14, 5))
plt.plot(yearly['year'], yearly['value'], marker='o', color='steelblue', linewidth=2)
plt.title('Yearly Sales Trend (1992-2024)', fontsize=16)
plt.xlabel('Year')
plt.ylabel('Total Value')
plt.tight_layout()
plt.savefig(base + r'\reports\yearly_trend.png')
plt.show()
print("✅ Plot 1 saved!")

# ── Plot 2: Top 10 Businesses ──────────────────────────
top_biz = df.groupby('kind_of_business')['value'].sum().nlargest(10)

plt.figure(figsize=(12, 6))
sns.barplot(x=top_biz.values, y=top_biz.index, palette='viridis')
plt.title('Top 10 Businesses by Total Value', fontsize=16)
plt.xlabel('Total Value')
plt.ylabel('')
plt.tight_layout()
plt.savefig(base + r'\reports\business_category.png')
plt.show()
print("✅ Plot 2 saved!")

# ── Plot 3: Monthly Sales Pattern ─────────────────────
df['month_num'] = df['month'].dt.month
monthly_avg = df.groupby('month_num')['value'].mean().reset_index()

plt.figure(figsize=(10, 5))
sns.barplot(x='month_num', y='value', data=monthly_avg, palette='coolwarm')
plt.title('Average Sales by Month', fontsize=16)
plt.xlabel('Month')
plt.ylabel('Average Value')
plt.xticks(ticks=range(12), labels=['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'])
plt.tight_layout()
plt.savefig(base + r'\reports\monthly_trends.png')
plt.show()
print("✅ Plot 3 saved!")

print("\n🎉 All plots saved in reports folder!")