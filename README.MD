# 🛒 Ecommerce Customer Intelligence Pipeline

An end-to-end ecommerce analytics pipeline built using Python, PostgreSQL, FastAPI and Power BI.

This project simulates a real-world data analytics workflow used in modern data-driven companies.

---

## 🚀 Project Overview

The goal of this project is to build a complete analytics system for ecommerce data that can:

- Process raw transaction data
- Clean and validate datasets
- Generate analytical features
- Detect abnormal transactions
- Segment customers based on purchasing behavior
- Store processed data in PostgreSQL
- Serve insights via FastAPI
- Visualize business metrics in Power BI

---

## 🏗 Project Architecture

Raw Data → Data Cleaning → Data Validation → Feature Engineering → Machine Learning → PostgreSQL → FastAPI → Power BI Dashboard

---

## 🧰 Tech Stack

Python  
Pandas  
NumPy  
Scikit-learn  
PostgreSQL  
FastAPI  
Power BI  
Git & GitHub  

---

## 📂 Project Structure

ecommerce-customer-intelligence  
│  
├── api  
│   └── main.py  

├── data  
│   ├── raw  
│   │   └── ecommerce_raw.csv  
│   │  
│   └── processed  
│       ├── ecommerce_cleaned.csv  
│       ├── ecommerce_validated.csv  
│       ├── customer_features.csv  
│       ├── customer_segments.csv  
│       └── anomalous_transactions.csv  

├── notebooks  
│   ├── eda_analysis.ipynb  
│   ├── customer_segmentation.ipynb  
│   └── anomaly_detection.ipynb  

├── src  
│   ├── data_generation.py  
│   ├── data_cleaning.py  
│   ├── data_validation.py  
│   └── load_to_postgres.py  

├── requirements.txt  
└── README.md  

---

## ⚙️ ETL Pipeline

Extract → Transform → Load

Extract  
Raw ecommerce transaction data is collected.

Transform  
Data cleaning and validation:
- Handle missing values
- Fix incorrect data types
- Ensure data consistency

Load  
Processed data is stored in PostgreSQL for analytics and dashboard use.

---

## 🤖 Machine Learning

### Customer Segmentation
Customers are grouped based on:

- Purchase frequency
- Total spending
- Average order value

### Anomaly Detection
Machine learning models detect abnormal transactions that may indicate fraud or unusual purchasing behaviour.

---

## 📊 Dashboard Insights

Power BI dashboards provide insights such as:

- Total Revenue
- Total Orders
- Average Order Value
- Monthly Sales Trends
- Top Customers
- Customer Segmentation
- Transaction Anomalies

---

## ▶ Running the Project

Install dependencies

pip install -r requirements.txt

Run data pipeline

python src/data_cleaning.py  
python src/data_validation.py  
python src/load_to_postgres.py  

Run API

uvicorn api.main:app --reload

API will run at:

http://127.0.0.1:8000

---

## 👨‍💻 Author

Kaustubh Singh  
GitHub: https://github.com/KaustubhSingh264

⭐ If you like this project, consider giving it a star!
