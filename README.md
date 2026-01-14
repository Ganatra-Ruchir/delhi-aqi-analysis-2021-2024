

# 🌍 Delhi Air Quality Index (AQI) Analysis (2021–2024)

This repository contains a **comprehensive exploratory data analysis** of Delhi’s air quality between 2021 and 2024, focusing on long‑term trends, seasonal patterns, and relationships between key pollutants and overall AQI.[1]

***

## 📌 Project Overview

- 4 years of **daily AQI data** for Delhi (1,461 observations, 2021‑01‑01 to 2024‑12‑31).[1]
- Detailed analysis of major pollutants: PM2.5, PM10, NO2, SO2, CO, and Ozone.[1]
- Clean, well‑structured dataset with **0 missing values** and multiple engineered features for richer insights.[1]
- Jupyter notebooks and a Streamlit app for both exploratory and presentation‑ready analysis.[1]

This project is designed as a portfolio‑quality EDA case study, suitable for showcasing data analysis, visualization, and communication skills.

***

## 📂 Repository Structure

```text
.
├── notebooks/                   # Jupyter analysis notebooks
│   ├── 01_Interactive_EDA.ipynb          # Main exploratory analysis
│   ├── 02_Statistical_Analysis.ipynb     # Hypothesis tests & correlations
│   └── 03_Advanced_Visualizations.ipynb  # Publication-ready plots
│
├── data/
│   ├── raw/
│   │   └── delhi_air_quality_clean.csv   # Original dataset (1,461 × 12)
│   └── processed/
│       ├── aqi_cleaned.csv               # Processed dataset (1,461 × 21)
│       └── data_summary.txt              # Processing summary
│
├── config/
│   ├── __init__.py
│   └── config.py              # Centralized paths & project settings
│
├── images/
│   └── plots/                 # Generated charts & figures
│
├── docs/
│   ├── README.md              # Project documentation (this file)
│   ├── PIPELINE_STATUS.md     # Data pipeline details
│   └── DATA_CLEANING_REPORT.md# Data cleaning procedures
│
├── app.py                     # Streamlit dashboard
├── requirements.txt           # Python dependencies
└── .gitignore
```



***

## 📊 Dataset & Features

**Core dataset**

- Records: **1,461 daily observations**.[1]
- Time span: **2021‑01‑01 → 2024‑12‑31**.[1]
- Original columns: **12**; after feature engineering: **21**.[1]
- Missing values: **0** (fully complete).[1]

**Pollutants**

- PM2.5, PM10, NO2, SO2, CO, Ozone.[1]

**Key engineered features**

- `DateTime`: Standardized datetime column.[1]
- `Season`: Categorical (Winter, Summer, Monsoon, Autumn).[1]
- `AQI_Category`: Good, Satisfactory, Moderately Polluted, Poor, Very Poor, Severe.[1]
- `IsWeekend`: Boolean weekday/weekend flag.[1]
- `AvgPollution`: Mean concentration across the six pollutants.[1]

***

## 🔍 Analysis Highlights

**Air quality status**

- Good days: ~15% of observations.[1]
- Moderately polluted: ~45% of observations.[1]
- Poor to severe: ~40% of observations.[1]

**Seasonal patterns**

- Worst season: **Winter (Dec–Feb)** with average AQI often above 200.[1]
- Best season: **Summer (Mar–May)** with AQI typically between 100–150.[1]
- Monsoon shows moderate improvement but remains variable.[1]

**Pollutant insights**

- Most critical pollutant: **PM2.5**, consistently at higher concentrations.[1]
- SO2 appears relatively well controlled with lower levels.[1]
- Strong positive correlations between AQI and PM2.5/PM10 (correlation coefficient \(r > 0.85\)).[1]

**Temporal patterns**

- Weekends show only a small improvement (~2–3% lower AQI than weekdays).[1]
- Clear worsening trend from 2021 to 2023, followed by slight improvement in 2024.[1]

***

## 📓 Notebooks

- `01_Interactive_EDA.ipynb`  
  - End‑to‑end interactive exploration: loading, cleaning, feature engineering, distributions, correlations, seasonal and temporal patterns, and key insights.[1]

- `02_Statistical_Analysis.ipynb`  
  - Formal hypothesis testing, correlation significance, distribution checks, and outlier analysis.[1]

- `03_Advanced_Visualizations.ipynb`  
  - Publication‑ready plots with custom styles, annotations, and layout refinements.[1]

- `generate_plots.ipynb`  
  - Lightweight notebook to generate core plots and save them to `images/plots/`.[1]

***

## 📈 Streamlit Dashboard

A Streamlit app (`app.py`) provides an interactive way to explore:[1]

- AQI trends over time.[1]
- Seasonal breakdowns.[1]
- Pollutant‑wise contributions and correlations.[1]

Run locally with:

```bash
streamlit run app.py
```



***

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/Ganatra-Ruchir/delhi-aqi-analysis-2021-2024.git
cd delhi-aqi-analysis-2021-2024
```



### 2. Create and activate environment

```bash
# Using venv
python -m venv venv
venv\Scripts\activate

# Or using conda
conda create -n aqi-analysis python=3.9
conda activate aqi-analysis
```



### 3. Install dependencies

```bash
pip install -r requirements.txt
```



### 4. Run notebooks or dashboard

```bash
# Streamlit dashboard
streamlit run app.py

# Notebooks
jupyter notebook notebooks/01_Interactive_EDA.ipynb
```



***

## 🧩 Configuration

Project‑wide paths and settings are centralized in `config/config.py`:[1]

- Raw data file paths.  
- Processed data locations.  
- Image output directories.  
- List of pollutants and AQI category thresholds.  

This makes it easier to change directories or extend the project without modifying multiple files.

***

## 📷 Key Visualizations

High‑resolution plots are generated and stored under `images/plots/`:[1]

- AQI distribution (histogram + box plot).  
- AQI category distribution.  
- Pollutant correlation heatmap.  
- Seasonal AQI analysis.  
- 4‑year AQI time series with moving average.  

These are suitable for reports, presentations, and dashboards.

***

## 🎯 Future Work

Potential extensions of this project:

1. **Forecasting**: ARIMA, Prophet, or machine learning models for AQI prediction.[1]
2. **Causal analysis**: Integrate weather, traffic, and policy data to understand drivers of pollution.[1]
3. **City‑level comparison**: Benchmark Delhi against other Indian cities.[1]
4. **Real‑time integration**: Connect to live AQI APIs and update dashboards automatically.[1]

***

## 📚 Attribution

- Data source: Delhi Air Quality Index (2021–2024).[1]
- Analysis period: January 2026.[1]

This repository is intended for educational and research purposes, and to demonstrate **end‑to‑end EDA and visualization** on a real‑world environmental dataset.

***
