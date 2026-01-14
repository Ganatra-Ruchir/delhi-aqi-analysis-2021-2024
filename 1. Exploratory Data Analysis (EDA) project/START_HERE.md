# 🚀 Quick Start Guide

## 3 Ways to Use This Project

### 1️⃣ **Dashboard** (Recommended) ⭐
```bash
streamlit run app.py
```
✅ **Best for**: Interactive exploration, filtering, real-time analysis
- 📊 Multiple tabs (Overview, Analysis, Pollutants, Seasonal)
- 🎛️ Year filter on sidebar
- 📈 KPI cards and key metrics
- 🎨 Beautiful, interactive visualizations
- ⏱️ Instant updates

### 2️⃣ **Generate Plots**
```bash
jupyter notebook generate_plots.ipynb
```
✅ **Best for**: Creating and saving publication-quality plots
- 5 steps: Setup → Load → Prepare → Generate Plots → Done
- 📸 Generates 5 PNG files (150 DPI)
- 💻 Simple, readable code (easy to modify)
- 🎯 Perfect for presentations

**Saves to**: `images/plots/`
- 01_aqi_distribution.png
- 02_category_breakdown.png
- 03_correlation_heatmap.png
- 04_seasonal_analysis.png
- 05_timeseries_trend.png

### 3️⃣ **Data Analysis Notebook**
```bash
jupyter notebook notebooks/01_Interactive_EDA.ipynb
```
✅ **Best for**: Deep exploration and understanding data
- 📊 Data loading and exploration
- ⚙️ Feature engineering
- 📈 Distribution analysis
- 🔗 Correlation analysis
- 📅 Seasonal patterns
- 📑 Summary and insights

---

## 📝 Code Simplification

### Before (Complex) ❌
```python
# Lots of parameters
fig, axes = plt.subplots(1, 2, figsize=(14, 5))
axes[0].hist(df['AQI'], bins=50, color='steelblue', edgecolor='black', alpha=0.7)
axes[0].axvline(df['AQI'].mean(), color='red', linestyle='--', linewidth=2, 
                label=f'Mean: {df["AQI"].mean():.1f}')
# ... many more lines
```

### After (Simple) ✅
```python
# Clear, short code
fig, ax = plt.subplots(figsize=(12, 4))
ax.hist(df['AQI'], bins=40, color='steelblue', alpha=0.7)
ax.axvline(df['AQI'].mean(), color='red', linestyle='--', label=f'Mean: {df["AQI"].mean():.0f}')
ax.set_title('AQI Distribution')
ax.grid(alpha=0.3)
plt.show()
```

---

## 🎛️ Dashboard Features

### Top KPIs
- 📈 Average AQI
- 🎯 Max AQI
- 📍 Min AQI
- 📊 Total Days

### Tabs
1. **Overview**: Histogram & Box Plot
2. **Analysis**: Category breakdown with percentages
3. **Pollutants**: Statistics & correlation with AQI
4. **Seasonal**: Box plots & statistics by season

### Sidebar
- 🎚️ Filter by year(s)
- Real-time updates

---

## 📊 What Each File Does

| File | Purpose | Use |
|------|---------|-----|
| `app.py` | Streamlit dashboard | `streamlit run app.py` |
| `generate_plots.ipynb` | Generate plots | `jupyter notebook generate_plots.ipynb` |
| `01_Interactive_EDA.ipynb` | Explore data | `jupyter notebook notebooks/01_Interactive_EDA.ipynb` |
| `README.md` | Documentation | Open in editor |

---

## 🎓 Learning Path

1. **Start**: Run dashboard → understand data visually
2. **Explore**: Run notebooks → see how visualizations are made
3. **Modify**: Change colors, filters, plots in code
4. **Create**: Build your own analysis

---

## ⚡ Installation (One-time)

```bash
# Install dependencies
pip install -r requirements.txt

# That's it!
```

---

## 🆘 Common Issues

| Issue | Fix |
|-------|-----|
| `streamlit: command not found` | Run: `pip install streamlit` |
| `ModuleNotFoundError: No module named 'pandas'` | Run: `pip install -r requirements.txt` |
| `FileNotFoundError: data/raw/...` | Make sure you're in project root folder |

---

## 🎯 Recommended Order

1. ✅ Run dashboard: `streamlit run app.py`
2. ✅ Explore data with filters
3. ✅ Generate plots: `jupyter notebook generate_plots.ipynb`
4. ✅ Learn code: `jupyter notebook notebooks/01_Interactive_EDA.ipynb`

---

**Let's go!** 🚀

Pick any option above and get started!
