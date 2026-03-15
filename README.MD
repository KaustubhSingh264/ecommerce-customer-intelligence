🛒 Ecommerce Customer Intelligence Pipeline

An end-to-end ecommerce analytics pipeline built using Python, PostgreSQL, FastAPI, and Power BI.

This project simulates a real-world data analytics workflow used in modern data-driven companies where raw data is processed through an ETL pipeline, stored in a database, analyzed using machine learning, and visualized using dashboards.

---

🚀 Project Overview

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

🏗 Project Architecture

Raw Data
↓
Data Cleaning
↓
Data Validation
↓
Feature Engineering
↓
Machine Learning
↓
PostgreSQL
↓
FastAPI
↓
Power BI Dashboard

---

🧰 Tech Stack

Programming

- Python

Data Processing

- Pandas
- NumPy

Machine Learning

- Scikit-learn

Database

- PostgreSQL

Backend

- FastAPI

Visualization

- Power BI

Tools

- Git
- GitHub
- Jupyter Notebook

---

📂 Project Structure

ecommerce-customer-intelligence/
│
├── api/
│   └── main.py
│
├── data/
│   ├── raw/
│   │   └── ecommerce_raw.csv
│   │
│   └── processed/
│       ├── ecommerce_cleaned.csv
│       ├── ecommerce_validated.csv
│       ├── customer_features.csv
│       ├── customer_segments.csv
│       └── anomalous_transactions.csv
│
├── notebooks/
│   ├── eda_analysis.ipynb
│   ├── customer_segmentation.ipynb
│   └── anomaly_detection.ipynb
│
├── src/
│   ├── data_generation.py
│   ├── data_cleaning.py
│   ├── data_validation.py
│   └── load_to_postgres.py
│
├── dashboard/
│   └── ecommsales1.pdf
│
├── requirements.txt
└── README.md

---

⚙️ ETL Pipeline

The project follows a structured ETL workflow (Extract → Transform → Load).

Extract

Raw ecommerce transaction data is collected.

Transform

Data cleaning and validation steps include:

- Handling missing values
- Fixing incorrect data types
- Ensuring data consistency

Load

Processed data is stored in PostgreSQL for analytics and dashboard use.

---

🤖 Machine Learning

Customer Segmentation

Customers are grouped based on purchasing behavior using clustering techniques.

Key features used:

- Purchase frequency
- Total spending
- Average order value

This helps businesses identify:

- High-value customers
- Regular customers
- Occasional buyers

---

Anomaly Detection

Machine learning models detect abnormal transactions that may indicate:

- Fraudulent transactions
- Unusual purchasing patterns
- Data anomalies

---

📊 Dashboard Insights

Power BI dashboards provide insights such as:

- Total Revenue
- Total Orders
- Average Order Value
- Monthly Sales Trends
- Top Customers
- Customer Segmentation
- Transaction Anomalies

---

📊 Power BI Dashboard

The final stage of this project is a Power BI dashboard that visualizes insights generated from the analytics pipeline.

After the ETL pipeline processes the ecommerce data and loads it into PostgreSQL, the dataset is used to create interactive visualizations in Power BI.

The dashboard helps businesses understand:

- Sales performance
- Customer behavior
- Product trends

Key Dashboard Features

- Sales Forecast Trend – Predicts future revenue trends using historical data.
- Revenue Over Time – Shows how sales change across time.
- Profit by City – Identifies cities generating the highest profit.
- Top Product Categories – Shows the best-performing categories.
- Customer Purchase Patterns – Highlights spending behavior of customers.
- Product Rating Distribution – Shows product satisfaction levels.

Dashboard File

The Power BI dashboard is included in this repository as a PDF:

dashboard/ecommsales1.pdf

---

▶ Running the Project

Install dependencies

pip install -r requirements.txt

Run the ETL pipeline

python src/data_cleaning.py
python src/data_validation.py
python src/load_to_postgres.py

Run the API

uvicorn api.main:app --reload

API will run locally at:

http://127.0.0.1:8000

---

👨‍💻 Author

Kaustubh Singh

GitHub
https://github.com/KaustubhSingh264

---

⭐ If you found this project useful, consider giving it a star on GitHub.
