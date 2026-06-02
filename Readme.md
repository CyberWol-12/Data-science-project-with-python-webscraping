# Data-science-project-with-python-webscraping

##  Project Overview

This project focuses on scraping homestay data from 9 different states of the USA and performing complete end-to-end data analysis using Python, PostgreSQL, and Data Science libraries.

The project includes:

- Web Scraping using BeautifulSoup
- Data Cleaning & Preprocessing
- Exploratory Data Analysis (EDA)
- PostgreSQL Database Integration
- CSV Dataset Generation
- Visualization & Statistical Analysis

The final cleaned dataset was stored as:
homestay.csv



#  States Covered

The homestay datasets were scraped from the following USA states/cities:

1. New York
2. San Francisco
3. San Diego
4. Washington
5. Las Vegas
6. Miami
7. Albuquerque
8. Indianapolis
9. Philadelphia

#  Project Structure

```
USA_Diff_States_webscrape/

├── 01_New_York.csv
├── 02_San_Francisco.csv
├── 03_San_Diego.csv
├── 04_Washington.csv
├── 05_Las_Vegas.csv
├── 06_Miami.csv
├── 07_albuquerque.csv
├── 08_Indianapolis.csv
├── 09_Philadelphia.csv
├── homestay.csv
├── homestay.ipynb

└── README.md
```


# Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- BeautifulSoup
- Requests
- SQLAlchemy
- PostgreSQL


#  Dataset Columns & Meaning

### visitor
Footprint of active users and demand-related metrics.

### Criteria(%)
Matching or quality ratings parsed from string format (`XX%`) into raw mathematical float values.

### Homestay(seasonal)
Represents rental scheduling patterns and seasonal availability metrics.

### Available_for
Target user segmentation and customer availability patterns.

### House_facilities
Structured feature mapping for homestay utilities and building facilities.

### absolute_link
Direct homestay listing URL collected during web scraping.


#  Web Scraping Workflow

The project uses BeautifulSoup and Requests library for extracting homestay data.

## Steps Performed

1. Sending HTTP requests
2. Parsing HTML content
3. Extracting homestay information
4. Cleaning scraped data
5. Combining all state datasets
6. Creating centralized dataset


# Data Cleaning & Preprocessing

The scraped dataset contained messy and inconsistent data.

The following preprocessing operations were performed:

- Removed missing values
- Converted datatypes
- Removed duplicates
- Parsed percentage columns
- Cleaned string columns
- Standardized column naming
- Managed categorical data


# Exploratory Data Analysis (EDA)

Performed multiple analyses such as:

- Mean calculation
- Frequency analysis
- Histogram plotting
- Bar chart visualization
- Seasonal availability analysis
- Criteria percentage analysis
- Distribution analysis

Visualization library used:
Matplotlib




#  PostgreSQL Integration

The cleaned dataset was stored inside PostgreSQL database using SQLAlchemy.

## PostgreSQL Connection Example


from sqlalchemy import create_engine

engine = create_engine(
    'postgresql+psycopg2://postgres:password@localhost:5432/postgres'
)

real_estate_df.to_sql(
    'real_estate',
    engine,
    if_exists='replace',
    index=False
)

# Final Outputs

- Centralized CSV Dataset
- PostgreSQL Database Table
- Visualized Graphs
- Statistical Insights
- Cleaned Structured Dataset


#  Outcome

This project helped in understanding:

- Real-world web scraping
- Data preprocessing techniques
- Handling messy datasets
- PostgreSQL database integration
- Exploratory Data Analysis
- End-to-end Data Science workflow


# Libraries Used

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from bs4 import BeautifulSoup
import requests
from sqlalchemy import create_engine

# Conclusion

This project demonstrates a complete real-world data science pipeline starting from web scraping to database integration and visualization.

It helped in gaining practical exposure to:

- Web scraping
- Data cleaning
- Data analysis
- PostgreSQL
- Visualization
- Real-world dataset handling