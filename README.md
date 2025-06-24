📊 Data_Driven_Stock_Analysis: Pandas + Streamlit + Power BI

This project provides a comprehensive data-driven analysis of Nifty 50 stock performance, combining data wrangling using Python (Pandas in Google Colab), interactive frontend using Streamlit, and insightful business intelligence visuals using Power BI.

![image](https://github.com/user-attachments/assets/b08666f1-77d8-45fa-961b-fa2302cc3393)


---

## 🔍 Project Objective
To analyze, visualize, and interactively explore the performance of Nifty 50 stocks over time. The project aids investors, analysts, and enthusiasts in identifying top performers, volatile stocks, and sector-wise trends using both automated and visual tools.

---

## 🧱 Components Overview

### 🔹 1. Data Engineering (Google Colab - Python)
- Raw YAML data transformed into structured CSVs using Pandas
- Feature engineering (daily return, cumulative return, volatility)
- Sector mapping and time-based aggregation (monthly trends)
- Output: `combined_stocks.csv`, `engineered_stocks.csv`, `volatility.csv`, `monthly_return.csv`, `sector_mapping.csv`

### 🔹 2. Interactive Dashboard (Streamlit)
- Real-time dashboard using `app.py`
- Visual tabs include:
  - Top 10 Gainers and Losers
  - Volatility Heatmap
  - Monthly Top Movers (via dropdown selection)
  - Stock Correlation Matrix (Seaborn heatmap)
  - Sector-wise Return Overview
- Hosted locally or deployable via Streamlit Cloud

### 🔹 3. Business Intelligence Visualization (Power BI)
- Imported engineered data for visuals:
  - Top/Bottom Performers by Return
  - Most Volatile Stocks (with custom RANKX)
  - Monthly Insights via Slicer
  - Sector-Wise Performance using external sector mapping
- Dynamic filters, responsive slicers, professional layout

---

## 📁 Datasets Used

| File | Description |
|------|-------------|
| `combined_stocks.csv` | Consolidated OHLCV stock data |
| `engineered_stocks.csv` | Includes cumulative return, sector mapping |
| `monthly_return.csv` | Monthly performance summary |
| `volatility.csv` | Daily return standard deviation |
| `sector_mapping.csv` | Mapping of Ticker to Sector |

---

## ⚙️ Technologies Used

| Layer | Tools |
|-------|-------|
| Programming | Python, Pandas |
| Notebook | Google Colab |
| Dashboard | Streamlit |
| BI Visualization | Power BI |
| Libraries | Matplotlib, Seaborn, DAX, Power Query |

---

## 💡 Key Features
- End-to-end ETL pipeline from YAML to visual dashboard
- Interactive UI for non-technical users (Streamlit)
- Visual storytelling using BI principles (Power BI)
- Clean DAX logic with TOPN and RANKX implementation

---

## 📈 Outcome
A fully functional multi-platform analytics tool that enables stock performance comparison, monthly tracking, sector evaluation, and volatility assessment — tailored for finance-focused decision making.

---

> ✅ This project is part of a professional data portfolio showcasing Python automation, interactive dashboards, and business-ready visual insights.

"""

# Save to markdown
readme_full_path = Path("/mnt/data/README_Full_Stock_Project.md")
readme_full_path.write_text(readme_full_content)

readme_full_path
