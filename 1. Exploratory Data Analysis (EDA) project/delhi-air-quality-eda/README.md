# Delhi Air Quality - Exploratory Data Analysis

Comprehensive EDA on Delhi air quality data (2021-2023) analyzing PM2.5, PM10, NO2, SO2, CO, Ozone, and AQI with interactive visualizations.

## 📊 Dataset

- **Records**: 1,461 daily observations
- **Columns**: 12 (pollutants, AQI, holidays)
- **Date Range**: 2021-2023
- **File**: `final_dataset.csv`

**Columns:**
- `Date`, `Month`, `Year` - Temporal info
- `PM2.5`, `PM10`, `NO2`, `SO2`, `CO`, `Ozone` - Pollutants
- `AQI` - Air Quality Index
- `Holidays_Count` - Holiday days
- `Days` - Day of month

---

## 🚀 Quick Start

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Run EDA Notebook
```bash
jupyter notebook notebooks/eda_delhi_air_quality.ipynb
```
**Generates:**
- Statistical analysis
- 5 visualization PNG files
- 1 interactive HTML file
- Processed dataset

### 3. Launch Dashboard
```bash
streamlit run app/dashboard.py
```
**Features:**
- Real-time filtering
- 4 analysis tabs
- Interactive charts
- Data export

---

## 📁 Project Structure

```
delhi-air-quality-eda/
├── final_dataset.csv           Main dataset (1,461 records)
├── notebooks/
│   └── eda_delhi_air_quality.ipynb    Main analysis notebook
├── app/
│   └── dashboard.py             Interactive Streamlit dashboard
├── src/
│   └── data_utils.py            Helper functions
├── data/
│   ├── raw/                     Raw data storage
│   └── processed/               Cleaned data
├── images/plots/                Generated visualizations
├── requirements.txt             Dependencies
├── README.md                    This file
├── LICENSE                      MIT License
└── .gitignore                   Git exclude rules
```

---

## 📈 Analysis Included

### 1. Data Overview
- 1,461 records spanning 3 years
- 12 features including 6 pollutants
- Zero missing values

### 2. Pollution Analysis
- **PM2.5**: Fine particulate matter (avg ~200)
- **PM10**: Coarse particulate (avg ~250)
- **NO2**: Nitrogen dioxide (avg ~125)
- **SO2**: Sulfur dioxide (avg ~10)
- **CO**: Carbon monoxide (avg ~1.2)
- **Ozone**: Ground-level ozone (avg ~45)

### 3. AQI Insights
- **Range**: 149-482
- **Average**: ~302
- **Monthly patterns**: Winter worst (Dec-Jan)
- **Yearly trends**: 2021-2023 comparison

### 4. Holiday Impact
- Effect on AQI during holidays
- Pollutant level differences
- Comparative analysis

### 5. Correlations
- Pollutant relationships
- AQI drivers
- Seasonal patterns

---

## 📊 Visualizations

| File | Description |
|------|-------------|
| `pollutants_distribution.png` | Histograms of all pollutants |
| `pollutants_correlation_heatmap.png` | Correlation matrix |
| `aqi_trend_over_time.png` | Time series trends |
| `aqi_by_month.html` | Interactive monthly AQI |
| `holiday_impact.png` | Holiday vs normal days |

---

## 🎯 Key Findings

1. **Winter pollution peaks** in Dec-Jan
2. **PM2.5 & PM10 highly correlated** (0.89)
3. **Holidays reduce pollution** by ~15 AQI points
4. **Improving trend** from 2021 to 2023

---

## 📝 Usage Examples

### Load and explore data:
```python
from src.data_utils import load_data, clean_data
df = load_data('final_dataset.csv')
df_clean = clean_data(df)
```

### Get statistics:
```python
df_clean.describe()
```

### Create visualizations:
```python
import matplotlib.pyplot as plt
plt.hist(df_clean['PM2.5'], bins=30)
plt.show()
```

---

## 🛠️ Tools Used

- **Python 3.13**
- **Pandas**: Data manipulation
- **NumPy**: Numerical operations
- **Matplotlib**: Static plots
- **Seaborn**: Statistical plots
- **Plotly**: Interactive visualizations
- **Streamlit**: Web dashboard

---

## 📄 License

MIT License - See LICENSE file for details

---

## 👨‍💻 Author

Created: January 2026
