import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# ── Load Clean Data ────────────────────────────────────
base = r'C:\Users\KRISH\OneDrive\Music\Desktop\retail and food services\retail-analysis'
df = pd.read_csv(base + r'\data\retail_clean.csv', parse_dates=['month'])
df['year'] = df['month'].dt.year
df['month_num'] = df['month'].dt.month

os.makedirs(base + r'\reports', exist_ok=True)
sns.set_theme(style='darkgrid')

# ── Trend 1: Yearly Growth Rate ────────────────────────
yearly = df.groupby('year')['value'].sum().reset_index()
yearly['growth_%'] = yearly['value'].pct_change() * 100

plt.figure(figsize=(14, 5))
plt.bar(yearly['year'], yearly['growth_%'], color='steelblue')
plt.axhline(0, color='red', linewidth=1)
plt.title('Yearly Growth Rate (%)', fontsize=16)
plt.xlabel('Year')
plt.ylabel('Growth %')
plt.tight_layout()
plt.savefig(base + r'\reports\yearly_growth.png')
plt.show()
print("✅ Trend 1 saved!")

# ── Trend 2: Top 5 Business Trends Over Time ───────────
top5 = df.groupby('kind_of_business')['value'].sum().nlargest(5).index
df_top5 = df[df['kind_of_business'].isin(top5)]

pivot = df_top5.groupby(['year', 'kind_of_business'])['value'].sum().unstack()

plt.figure(figsize=(14, 6))
for col in pivot.columns:
    plt.plot(pivot.index, pivot[col], marker='o', label=col)
plt.title('Top 5 Businesses Trend Over Time', fontsize=16)
plt.xlabel('Year')
plt.ylabel('Total Value')
plt.legend(fontsize=7, loc='upper left')
plt.tight_layout()
plt.savefig(base + r'\reports\top5_business_trend.png')
plt.show()
print("✅ Trend 2 saved!")

# ── Trend 3: Pre vs Post COVID ─────────────────────────
df['period'] = df['year'].apply(lambda x: 'Pre-COVID' if x < 2020 else 'Post-COVID')

period_data = df.groupby(['period', 'kind_of_business'])['value'].sum().reset_index()
top5_period = period_data[period_data['kind_of_business'].isin(top5)]

plt.figure(figsize=(14, 6))
sns.barplot(data=top5_period, x='kind_of_business', y='value', hue='period', palette='coolwarm')
plt.title('Pre vs Post COVID Sales (Top 5 Businesses)', fontsize=16)
plt.xlabel('')
plt.ylabel('Total Value')
plt.xticks(rotation=20, ha='right', fontsize=8)
plt.tight_layout()
plt.savefig(base + r'\reports\pre_post_covid.png')
plt.show()
print("✅ Trend 3 saved!")

print("\n🎉 Trend Analysis complete!")