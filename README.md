# 🛒 Retail & Food Services Sales Analysis (1992–2024)

> 📊 32 years of U.S. Retail data — cleaned, analyzed, and visualized using Python.

---

## 🚀 What This Project Does

Ever wondered how U.S. retail sales have grown over 3 decades?  
This project digs deep into **14,000+ rows** of real retail data and uncovers:

- 📈 How sales **4x'd** from 1992 to 2024
- 🚗 Which business categories **dominate** the market
- 📉 How the **2008 recession** and **COVID-19** impacted sales
- 🗓️ Which months see the **highest consumer spending**

---

## 📸 Snapshots

| Yearly Trend | Top 10 Businesses |
|---|---|
| ![Yearly](https://github.com/Krish-1410/Retail-sales-analysis-/blob/main/retail%20and%20food%20services/Retail%20Analysis/reports/yearly_trend.png) | ![Business](reports/business_category.png) |

| Monthly Pattern | Pre vs Post COVID |
|---|---|
| ![Monthly](reports/monthly_trends.png) | ![COVID](reports/pre_post_covid.png) |

---

## 🔍 Key Insights

- 🏆 **Motor Vehicle & Parts Dealers** — #1 category across all years
- 📈 Sales grew from **$3.1M (1992)** → **$13.8M (2024)**
- 📉 **2009** was the only year with negative growth (recession)
- 🦠 **Post-COVID boom** — 2021 saw the highest single-year jump
- 🎄 **December** is consistently the highest sales month

---

## 🛠️ Tech Stack

![Python](https://img.shields.io/badge/Python-3.13-blue?logo=python)
![Pandas](https://img.shields.io/badge/Pandas-2.0-green?logo=pandas)
![Matplotlib](https://img.shields.io/badge/Matplotlib-3.7-orange)
![Seaborn](https://img.shields.io/badge/Seaborn-0.12-blue)
![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-orange?logo=jupyter)


retail-analysis/
│
├── 📂 data/
│   ├── retail.csv              ← Raw data
│   └── retail_clean.csv        ← Cleaned data
│
├── 📓 notebooks/
│   ├── 01_data_loading.ipynb   ← Load & Clean
│   ├── 02_eda.ipynb            ← Exploratory Analysis
│   └── 03_visualizations.ipynb ← Charts & Graphs
│
├── 🐍 scripts/
│   ├── data_cleaning.py        ← Cleaning pipeline
│   ├── eda.py                  ← EDA script
│   ├── visualization.py        ← Graphs
│   └── trend_analysis.py       ← Trend & Growth analysis
│
├── 📊 reports/                 ← All output graphs
├── requirements.txt
└── README.md


---

## ⚡ Quick Start

```bash
git clone https://github.com/yourusername/retail-analysis.git


pip install -r requirements.txt


python scripts/data_cleaning.py
python scripts/eda.py
python scripts/visualization.py
python scripts/trend_analysis.py
```

---

## 👨‍💻 Author

**Krish** — Aspiring Data Analyst  
📧 Feel free to connect!

---
