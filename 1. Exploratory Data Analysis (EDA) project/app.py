import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# type: ignore  # Suppress matplotlib/pandas type hints that are partially unknown

# Page config
st.set_page_config(page_title="AQI Dashboard", layout="wide")

# Title
st.title("🌍 Delhi Air Quality Index (AQI) Dashboard")
st.markdown("Interactive visualization of air quality data (2021-2024)")

# Load data
@st.cache_data
def load_data() -> pd.DataFrame:
    df = pd.read_csv('data/raw/delhi_air_quality_clean.csv')
    df['DateTime'] = pd.to_datetime(df[['Year', 'Month', 'Date']].rename(
        columns={'Date': 'day', 'Month': 'month', 'Year': 'year'}))
    return df

df = load_data()
POLLUTANTS = ['PM2.5', 'PM10', 'NO2', 'SO2', 'CO', 'Ozone']

# Sidebar
st.sidebar.header("📊 Filters")
year_filter = st.sidebar.multiselect("Select Year", sorted(df['Year'].unique()), default=sorted(df['Year'].unique()))
df_filtered = df[df['Year'].isin(year_filter)]

# KPIs
col1, col2, col3, col4 = st.columns(4)
col1.metric("📈 Average AQI", f"{df_filtered['AQI'].mean():.0f}")
col2.metric("🎯 Max AQI", f"{df_filtered['AQI'].max():.0f}")
col3.metric("📍 Min AQI", f"{df_filtered['AQI'].min():.0f}")
col4.metric("📊 Total Days", f"{len(df_filtered)}")

st.divider()

# Tab 1: Overview
tab1, tab2, tab3, tab4 = st.tabs(["Overview", "Analysis", "Pollutants", "Seasonal"])

with tab1:
    st.subheader("AQI Distribution")
    
    col1, col2 = st.columns(2)
    
    with col1:
        fig, ax = plt.subplots(figsize=(8, 5))
        ax.hist(df_filtered['AQI'], bins=40, color='steelblue', alpha=0.7, edgecolor='black')
        ax.axvline(df_filtered['AQI'].mean(), color='red', linestyle='--', linewidth=2, label=f'Mean: {df_filtered["AQI"].mean():.0f}')
        ax.set_xlabel('AQI')
        ax.set_ylabel('Frequency')
        ax.set_title('AQI Histogram')
        ax.legend()
        ax.grid(alpha=0.3)
        st.pyplot(fig)
    
    with col2:
        fig, ax = plt.subplots(figsize=(8, 5))
        ax.boxplot(df_filtered['AQI'])
        ax.set_ylabel('AQI')
        ax.set_title('AQI Box Plot')
        ax.grid(alpha=0.3)
        st.pyplot(fig)

with tab2:
    st.subheader("Category Breakdown")
    
    def get_category(aqi: float) -> str:
        if aqi <= 50: return 'Good'
        elif aqi <= 100: return 'Satisfactory'
        elif aqi <= 200: return 'Moderate'
        elif aqi <= 300: return 'Poor'
        else: return 'Very Poor'
    
    df_filtered['Category'] = df_filtered['AQI'].apply(get_category)
    cats = df_filtered['Category'].value_counts()
    
    fig, ax = plt.subplots(figsize=(10, 5))
    colors_dict = {'Good': 'green', 'Satisfactory': 'yellow', 'Moderate': 'orange', 'Poor': 'red', 'Very Poor': 'darkred'}
    colors = [colors_dict.get(c, 'gray') for c in cats.index]
    
    bars = ax.bar(cats.index, cats.values, color=colors, edgecolor='black')
    ax.set_ylabel('Days')
    ax.set_title('Air Quality Categories')
    
    for bar, val in zip(bars, cats.values):
        pct = (val / len(df_filtered)) * 100
        ax.text(bar.get_x() + bar.get_width()/2, bar.get_height(), f'{pct:.0f}%', 
                ha='center', va='bottom', fontsize=10)
    
    ax.grid(alpha=0.3)
    st.pyplot(fig)

with tab3:
    st.subheader("Pollutant Statistics")
    
    stats = df_filtered[POLLUTANTS].describe().T[['mean', 'min', 'max']]
    st.dataframe(stats, use_container_width=True)
    
    # Pollutant correlation with AQI
    st.subheader("Pollutant Correlation with AQI")
    corr = df_filtered[POLLUTANTS].corrwith(df_filtered['AQI']).sort_values(ascending=False)
    
    fig, ax = plt.subplots(figsize=(10, 5))
    corr.plot(kind='barh', ax=ax, color='steelblue')
    ax.set_xlabel('Correlation with AQI')
    ax.set_title('Pollutant-AQI Correlation')
    ax.grid(alpha=0.3)
    st.pyplot(fig)

with tab4:
    st.subheader("Seasonal Analysis")
    
    def get_season(m: int) -> str:
        if m in [12, 1, 2]: return 'Winter'
        elif m in [3, 4, 5]: return 'Summer'
        elif m in [6, 7, 8, 9]: return 'Monsoon'
        else: return 'Autumn'
    
    df_filtered['Season'] = df_filtered['Month'].apply(get_season)
    
    # Season stats
    st.write("**Average AQI by Season:**")
    season_stats = df_filtered.groupby('Season')['AQI'].agg(['mean', 'min', 'max', 'count'])
    st.dataframe(season_stats, use_container_width=True)
    
    # Box plot
    fig, ax = plt.subplots(figsize=(10, 5))
    season_order = ['Winter', 'Summer', 'Monsoon', 'Autumn']
    df_filtered_season = df_filtered.copy()
    df_filtered_season['Season'] = pd.Categorical(df_filtered_season['Season'], categories=season_order, ordered=True)
    
    sns.boxplot(data=df_filtered_season, x='Season', y='AQI', ax=ax, order=season_order)
    ax.set_title('AQI Distribution by Season')
    ax.grid(alpha=0.3)
    st.pyplot(fig)

st.divider()

# Time series
st.subheader("AQI Time Series")
df_sort = df_filtered.sort_values('DateTime')

fig, ax = plt.subplots(figsize=(14, 5))
ax.plot(df_sort['DateTime'], df_sort['AQI'], alpha=0.5, label='Daily AQI')
ma = df_sort['AQI'].rolling(30).mean()
ax.plot(df_sort['DateTime'], ma, color='red', linewidth=2, label='30-Day MA')
ax.set_xlabel('Date')
ax.set_ylabel('AQI')
ax.set_title('AQI Trend (2021-2024)')
ax.legend()
ax.grid(alpha=0.3)
plt.xticks(rotation=45)
st.pyplot(fig)

st.divider()

# Footer
st.info("📊 Dashboard generated from Delhi Air Quality Index analysis (2021-2024)")
