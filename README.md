# Used Car Price Analysis - Exploratory Data Analysis (EDA)

## Live Dashboard: https://exploratory-data-analysis-eda--app-ja7aob.streamlit.app/

##  Project Overview

This project is a detailed **Exploratory Data Analysis (EDA)** of a dataset containing listings of used cars from different cities in India. The goal is to understand the key factors that influence the **price** of used cars and to prepare the dataset for potential predictive modeling in the future.

---

##  Dataset Description

The dataset contains real-world data about used cars, including various features such as brand, engine capacity, mileage, and ownership history.

###  Key Features:
- `Name`: Car brand and model  
- `Location`: City of sale  
- `Year`: Year of manufacture  
- `Kilometers_Driven`: Total distance the car has been driven  
- `Fuel_Type`: Fuel used (Petrol, Diesel, CNG, etc.)  
- `Transmission`: Manual or Automatic  
- `Owner_Type`: Number of previous owners  
- `Mileage`: Fuel efficiency (e.g., kmpl)  
- `Engine`: Engine size (cc)  
- `Power`: Engine power (bhp)  
- `Seats`: Number of seats  
- `New_Price`: Price when new (may be missing)  
- `Price`: Current market price (Target variable)  

---

##  Objectives

- Understand data structure and quality  
- Handle missing values and duplicates  
- Analyze numerical and categorical features  
- Explore data visually using graphs and plots  
- Study relationships between features  
- Identify outliers and inconsistencies  
- Derive insights for predictive modeling  

---

##  Tasks Performed

### Data Cleaning
- Loaded and explored data structure  
- Handled missing values and cleaned inconsistent data  
- Removed duplicate rows  

###  Descriptive Analysis
- Generated summary statistics (mean, median, std dev, etc.)  
- Analyzed frequency of categorical values like fuel type and owner type  

###  Visual Explorations
- Histograms and box plots for Price, Engine, Mileage  
- Bar charts for Fuel_Type, Transmission, and Owner_Type  
- Price trends over manufacturing years  
- Price comparisons across locations and fuel types  

###  Correlation & Feature Relationships
- Correlation heatmap for numeric columns  
- Scatter plots for Price vs Mileage, Power, Engine  
- Multivariate analysis (e.g., Fuel_Type & Transmission impact on Price)  

###  Outlier & Data Quality Checks
- Identified outliers using boxplots  
- Investigated units inconsistencies in features like Mileage and Power  
- Examined missing values in `New_Price` and potential effects  

###  Insights & Trends
- Identified most and least expensive models  
- Compared prices based on ownership history  
- Evaluated efficiency vs car age and price  

###  Predictive Readiness
- Suggested useful features for predictive modeling  
- Evaluated potential of using `New_Price` to estimate depreciation  
- Suggested feature encoding and engineering strategies  

---

##  Outcomes

- Deep insights into how factors like mileage, engine size, fuel type, and ownership affect car prices  
- Identification of strong predictors for price estimation  
- Prepared dataset for machine learning tasks  

---

##  Files Included

- `Car EDA Test Case.ipynb` – Jupyter Notebook with full analysis, code, and visualizations  
- `used_cars_data.csv` – Cleaned dataset of used cars  
- `Case problem statement.pdf` – Original problem description and task requirements  

---

##  Next Steps

- Build a machine learning model to predict car prices  
- Use feature engineering to improve model accuracy  
- Explore advanced techniques like regression and ensemble models  

---


