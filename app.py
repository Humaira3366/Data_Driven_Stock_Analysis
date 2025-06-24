import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

st.set_page_config(page_title="AI_ML Data Driven Stock Analysis", layout="wide", page_icon="📈")

# Load Data
df = pd.read_csv("engineered_stocks.csv", parse_dates=['date'])
volatility = pd.read_csv("volatility.csv")
monthly = pd.read_csv("monthly_return.csv")

st.title("📊 AI_ML Data Driven Stock Analysis")

# Tabs for navigation
tab1, tab2, tab3, tab4, tab5 = st.tabs(["🏆 Gainers/Losers", "📉 Volatility", "📆 Monthly Trends", "🧪 Correlation", " 📈 Sector-Wise Performance"])

# Tab 1: Gainers/Losers
with tab1:
    st.subheader("Top 10 Gainers & Losers")
    final_returns = df.groupby('Ticker')['cumulative_return'].last().reset_index()
    top_gainers = final_returns.sort_values(by='cumulative_return', ascending=False).head(10)
    top_losers = final_returns.sort_values(by='cumulative_return', ascending=True).head(10)

    col1, col2 = st.columns(2)
    with col1:
        st.markdown("#### 🚀 Top 10 Gainers")
        st.bar_chart(top_gainers.set_index('Ticker'))
    with col2:
        st.markdown("#### 📉 Top 10 Losers")
        st.bar_chart(top_losers.set_index('Ticker'))

# Tab 2: Volatility
with tab2:
    st.subheader("📉 Top 10 Most Volatile Stocks")
    top_vol = volatility.sort_values('volatility', ascending=False).head(10)
    st.bar_chart(top_vol.set_index('Ticker'))

# Tab 3: Monthly Top Movers
with tab3:
    st.subheader("📆 Monthly Gainers/Losers")
    selected_month = st.selectbox("Select Month", monthly['month'].unique())
    month_data = monthly[monthly['month'] == selected_month]
    top_5 = month_data.sort_values('daily_return', ascending=False).head(5)
    bottom_5 = month_data.sort_values('daily_return', ascending=True).head(5)

    col1, col2 = st.columns(2)
    with col1:
        st.markdown("##### 📈 Top 5 Gainers")
        st.bar_chart(top_5.set_index('Ticker')['daily_return'])
    with col2:
        st.markdown("##### 📉 Top 5 Losers")
        st.bar_chart(bottom_5.set_index('Ticker')['daily_return'])

# Tab 4: Correlation
with tab4:
    st.subheader("🧪 Stock Price Correlation Heatmap")
    pivot_df = df.pivot(index='date', columns='Ticker', values='close').pct_change()
    corr_matrix = pivot_df.corr()
    st.write("### 🔥 Heatmap of Stock Correlations")
    fig, ax = plt.subplots(figsize=(10, 8))
    sns.heatmap(corr_matrix, cmap="coolwarm", ax=ax)
    st.pyplot(fig)

# Tab 5: Sector-wise Performance
with tab5:
     st.subheader("📊 Sector-wise Average Yearly Return")

    # Sector Mapping
     sector_mapping = {
    'ADANIPORTS': 'Infrastructure',
    'ASIANPAINT': 'Consumer Goods',
    'AXISBANK': 'Financials',
    'BAJAJ-AUTO': 'Automobile',
    'BAJFINANCE': 'Financials',
    'BAJAJFINSV': 'Financials',
    'BHARTIARTL': 'Telecom',
    'BPCL': 'Energy',
    'BRITANNIA': 'Consumer Goods',
    'CIPLA': 'Pharmaceuticals',
    'COALINDIA': 'Energy',
    'DIVISLAB': 'Pharmaceuticals',
    'DRREDDY': 'Pharmaceuticals',
    'EICHERMOT': 'Automobile',
    'GRASIM': 'Cement',
    'HCLTECH': 'IT',
    'HDFC': 'Financials',
    'HDFCBANK': 'Financials',
    'HEROMOTOCO': 'Automobile',
    'HINDALCO': 'Metals',
    'HINDUNILVR': 'Consumer Goods',
    'ICICIBANK': 'Financials',
    'INDUSINDBK': 'Financials',
    'INFY': 'IT',
    'IOC': 'Energy',
    'ITC': 'Consumer Goods',
    'JSWSTEEL': 'Metals',
    'KOTAKBANK': 'Financials',
    'LT': 'Infrastructure',
    'M&M': 'Automobile',
    'MARUTI': 'Automobile',
    'NESTLEIND': 'Consumer Goods',
    'NTPC': 'Energy',
    'ONGC': 'Energy',
    'POWERGRID': 'Utilities',
    'RELIANCE': 'Energy',
    'SBILIFE': 'Financials',
    'SBIN': 'Financials',
    'SHREECEM': 'Cement',
    'SUNPHARMA': 'Pharmaceuticals',
    'TATACONSUM': 'Consumer Goods',
    'TATAMOTORS': 'Automobile',
    'TATASTEEL': 'Metals',
    'TCS': 'IT',
    'TECHM': 'IT',
    'TITAN': 'Consumer Goods',
    'ULTRACEMCO': 'Cement',
    'UPL': 'Chemicals',
    'WIPRO': 'IT'
}


     df['Sector'] = df['Ticker'].map(sector_mapping)

    # Calculate average sector return
     sector_performance = df.groupby('Sector')['cumulative_return'].mean().sort_values(ascending=False).reset_index()
     sector_performance.columns = ['Sector', 'Avg_Yearly_Return']

    # Plot
     fig, ax = plt.subplots(figsize=(10, 6))
     sns.barplot(data=sector_performance, x='Avg_Yearly_Return', y='Sector', palette='viridis', ax=ax)
     ax.set_title("Average Yearly Return by Sector", fontsize=14)
     ax.set_xlabel("Avg Yearly Return", fontsize=12)
     ax.set_ylabel("Sector", fontsize=12)
     st.pyplot(fig)