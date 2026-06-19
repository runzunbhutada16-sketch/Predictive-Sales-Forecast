# Predictive Sales Forecast and Business Intelligence System

A professional intermediate-to-advanced Python project for analyzing historical sales data and predicting future sales using **Machine Learning**, **Time Series Forecasting**, and **Business Intelligence** techniques.

This project combines **Data Analytics**, **EDA**, **Forecasting Models**, and **Interactive Visualizations** to help businesses make data-driven decisions.

---

##  Project Overview

The **Predictive Sales Forecast and Business Intelligence System** aims to:

* Analyze historical sales data.
* Identify sales trends and growth patterns.
* Evaluate product and regional performance.
* Forecast future sales using Machine Learning and Time Series models.
* Compare multiple forecasting models and select the best one.
* Generate business insights through visualizations and reports.

---

## Objectives

* Perform complete Exploratory Data Analysis (EDA).
* Build and compare forecasting models.
* Predict future sales for different time periods.
* Generate professional reports and visualizations.
* Follow industry-standard Python coding practices.

---

# Project Structure

```text
predictive-sales-forecast/
│
├── sales_forecast.py
├── sales_data.csv
│
├── models/
│   ├── linear_regression.pkl
│   ├── random_forest.pkl
│   ├── xgboost_model.pkl
│   ├── prophet_model.pkl
│   └── arima_model.pkl
│
├── reports/
│   ├── monthly_sales_report.csv
│   ├── yearly_sales_report.csv
│   ├── forecast_report.csv
│   └── model_comparison.csv
│
├── visualizations/
│
├── requirements.txt
└── README.md
```

---

#  Technologies Used

### Programming Language

* Python 3

### Libraries

* Pandas
* NumPy
* Matplotlib
* Seaborn
* Scikit-Learn
* XGBoost
* Prophet
* Statsmodels
* Tabulate
* Pickle

---

#  Dataset Structure

The project uses a CSV file named:

```text
sales_data.csv
```

### Sample Dataset

| Date       | Product  | Category    | Region | City      | Sales | Profit |
| ---------- | -------- | ----------- | ------ | --------- | ----: | -----: |
| 2024-01-05 | Laptop   | Electronics | North  | Delhi     | 45000 |   8000 |
| 2024-01-10 | Mouse    | Electronics | West   | Mumbai    |  1200 |    300 |
| 2024-02-15 | Keyboard | Electronics | South  | Bangalore |  2500 |    600 |
| 2024-03-08 | Monitor  | Electronics | East   | Kolkata   | 15000 |   2500 |

---

# Features

## 1. Data Cleaning and Preprocessing

✔ Handle missing values
✔ Remove duplicate records
✔ Handle invalid dates
✔ Detect and remove outliers
✔ Standardize product and region names

---

## 2. Exploratory Data Analysis (EDA)

The system calculates:

* Total Sales
* Monthly Sales
* Quarterly Sales
* Yearly Sales
* Sales Growth Rate (%)
* Average Revenue
* Average Order Value
* Profit Margin
* Revenue per Product
* Revenue per Region

---

## 3. Product Performance Analysis

Analyze:

* Best-Selling Products
* Top Revenue Generating Products
* Category-wise Sales
* Product Growth Trends

---

## 4. Regional Analysis

Analyze:

* Top Performing Regions
* Region-wise Revenue Distribution
* City-wise Sales Comparison

---

#  Forecasting Models

The project trains and compares:

| Model                   | Purpose                 |
| ----------------------- | ----------------------- |
| Linear Regression       | Baseline forecasting    |
| Random Forest Regressor | Non-linear forecasting  |
| XGBoost Regressor       | Advanced boosting model |
| Prophet                 | Time series forecasting |
| ARIMA                   | Statistical forecasting |

The best model is selected based on:

* MAE (Mean Absolute Error)
* RMSE (Root Mean Squared Error)
* R² Score

---

#  Future Sales Prediction

Predict future sales for:

* Next 30 Days
* Next 3 Months
* Next 6 Months
* Next 1 Year

Compare:

* Actual Sales
* Predicted Sales

Evaluate forecast accuracy using:

* MAE
* RMSE
* R² Score

---

# Visualizations

The project generates professional visualizations using Matplotlib and Seaborn.

### Sales Analysis

* Monthly Sales Trend Line Chart
* Quarterly Sales Comparison
* Yearly Sales Comparison
* Growth Rate Trend
* Revenue vs Profit Chart

### Product Analysis

* Top Products Bar Chart
* Category-wise Sales Chart

### Regional Analysis

* Pie Chart for Regional Revenue
* Horizontal Bar Chart for Top Regions

### Forecasting Analysis

* Actual vs Predicted Sales Plot
* Future Forecast Curve
* Residual Error Plot
* Model Comparison Chart

---

#  Dashboard Menu

The project includes an interactive terminal dashboard.

```text
===========================================
 PREDICTIVE SALES FORECAST SYSTEM
===========================================

1. View Dataset Summary
2. Analyze Sales Trends
3. Product Performance Analysis
4. Region-wise Analysis
5. Revenue and Profit Analysis
6. Train Forecasting Models
7. Predict Future Sales
8. Compare Forecast Models
9. Generate Visualizations
10. Export Reports
11. Exit
```

---

#  Reports Generated

Reports are automatically saved in the `reports/` folder.

Examples:

* monthly_sales_report.csv
* yearly_sales_report.csv
* forecast_report.csv
* model_comparison.csv

---

#  Installation

## Clone the Repository

```bash
git clone https://github.com/yourusername/predictive-sales-forecast.git

cd predictive-sales-forecast
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Run the Project

```bash
python sales_forecast.py
```

---

#  Example Output

```text
====================================================
PREDICTIVE SALES FORECAST SYSTEM
====================================================

 Loaded 500 records.

 Cleaning Dataset...

 Removed 5 rows with missing values.

 Removed 2 duplicate rows.

 Outliers removed.

 Dataset cleaned successfully.

 Final records: 493


 DATASET SUMMARY

+--------------------+------------------+
| Metric             | Value            |
+--------------------+------------------+
| Total Sales        | $1,250,450       |
| Total Profit       | $245,780         |
| Avg Revenue        | $2,536.41        |
| Unique Products    | 20               |
| Unique Regions     | 5                |
+--------------------+------------------+
```

---

#  Software Design Principles

The project follows:

* Object-Oriented Programming (OOP)
* PEP 8 Coding Standards
* Modular Code Structure
* Exception Handling
* Input Validation
* Reusable Functions
* Comprehensive Comments and Docstrings

---

# Future Enhancements

Potential improvements:

* Interactive Dashboard using Streamlit
* Real-time Sales Monitoring
* Deep Learning Models (LSTM)
* Deployment using Flask or FastAPI
* Interactive Forecasting Dashboard
* Cloud Deployment

AUTHOR: RUNZUN M. BHUTADA
INTERN-ID: CITS2504
