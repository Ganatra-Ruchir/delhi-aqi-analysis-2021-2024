"""
Configuration settings for AQI Data Analysis Pipeline
"""
import os
from pathlib import Path

# Project paths
PROJECT_ROOT = Path(__file__).parent.parent
DATA_DIR = PROJECT_ROOT / "data"
RAW_DATA_DIR = DATA_DIR / "raw"
PROCESSED_DATA_DIR = DATA_DIR / "processed"
SCRIPTS_DIR = PROJECT_ROOT / "scripts"
NOTEBOOKS_DIR = PROJECT_ROOT / "notebooks"
PLOTS_DIR = PROJECT_ROOT / "images" / "plots"

# Ensure directories exist
RAW_DATA_DIR.mkdir(parents=True, exist_ok=True)
PROCESSED_DATA_DIR.mkdir(parents=True, exist_ok=True)
PLOTS_DIR.mkdir(parents=True, exist_ok=True)

# File paths
RAW_DATA_FILE = RAW_DATA_DIR / "delhi_air_quality_clean.csv"
PROCESSED_DATA_FILE = PROCESSED_DATA_DIR / "aqi_cleaned.csv"
FEATURE_DATA_FILE = PROCESSED_DATA_DIR / "aqi_features.csv"

# Pollutant list
POLLUTANTS = ['PM2.5', 'PM10', 'NO2', 'SO2', 'CO', 'Ozone']

# AQI Categories
AQI_CATEGORIES = {
    'Good': (0, 50),
    'Satisfactory': (51, 100),
    'Moderately Polluted': (101, 200),
    'Poor': (201, 300),
    'Very Poor': (301, 400),
    'Severe': (401, float('inf'))
}

# Data cleaning parameters
MISSING_VALUE_THRESHOLD = 0.5  # 50% missing values threshold
OUTLIER_MULTIPLIER = 1.5  # IQR multiplier for outlier detection
ROLLING_WINDOW = 30  # Days for rolling average

# Visualization settings
PLOT_STYLE = 'seaborn-v0_8-darkgrid'
COLOR_PALETTE = 'husl'
FIGURE_SIZE = (14, 6)
DPI = 100
