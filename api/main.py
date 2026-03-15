from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.responses import StreamingResponse
import pandas as pd
import matplotlib
matplotlib.use("Agg")   # Important for macOS
import matplotlib.pyplot as plt
import io

# Initialize API
app = FastAPI(title="Ecommerce Customer Intelligence API")


# Response Models

class RevenueResponse(BaseModel):
    total_revenue: float

class DashboardSummaryResponse(BaseModel):
    total_revenue: float
    total_orders: int
    top_category: str
    average_rating: float


# Load datasets


try:
    df = pd.read_csv("data/processed/ecommerce_validated.csv")
    df["revenue"] = df["price"] * df["quantity"]
except Exception:
    df = pd.DataFrame()

try:
    anomalies = pd.read_csv("data/processed/anomalous_transactions.csv")
except Exception:
    anomalies = pd.DataFrame()

try:
    segments = pd.read_csv("data/processed/customer_segments.csv")
except Exception:
    segments = pd.DataFrame()



# Root Endpoint

@app.get("/")
def home():
    return {"message": "Ecommerce Analytics API is running 🚀"}



# Revenue Endpoint


@app.get("/revenue", response_model=RevenueResponse, tags=["Analytics"])
def total_revenue():

    if df.empty:
        return {"error": "Dataset not loaded"}

    total = df["revenue"].sum()

    return {"total_revenue": float(total)}



# Top Categories

@app.get("/top-categories")
def top_categories():

    if df.empty:
        return {"error": "Dataset not loaded"}

    revenue = (
        df.groupby("product_category")["revenue"]
        .sum()
        .sort_values(ascending=False)
    )

    return revenue.to_dict()



# Top Customers


@app.get("/top-customers")
def top_customers():

    if df.empty:
        return {"error": "Dataset not loaded"}

    customers = (
        df.groupby("customer_id")["revenue"]
        .sum()
        .sort_values(ascending=False)
        .head(10)
    )

    return customers.to_dict()



# Payment Method Distribution

@app.get("/payment-methods")
def payment_methods():

    if df.empty:
        return {"error": "Dataset not loaded"}

    methods = df["payment_method"].value_counts()

    return methods.to_dict()



# Anomaly Transactions

@app.get("/anomalies")
def anomaly_transactions():

    if anomalies.empty:
        return {"error": "Anomaly dataset not loaded"}

    return anomalies.head(20).to_dict(orient="records")


# Customer Segment

@app.get("/customer-segments")
def customer_segments():

    if segments.empty:
        return {"error": "Segmentation dataset not loaded"}

    result = segments["cluster"].value_counts()

    return result.to_dict()



# Chart Endpoint


@app.get("/charts/category-revenue")
def category_revenue_chart():

    if df.empty:
        return {"error": "Dataset not loaded"}

    revenue = (
        df.groupby("product_category")["revenue"]
        .sum()
        .sort_values(ascending=False)
    )

    plt.figure(figsize=(8, 5))
    revenue.plot(kind="bar")

    plt.title("Revenue by Product Category")
    plt.xlabel("Category")
    plt.ylabel("Revenue")
    plt.tight_layout()

    buffer = io.BytesIO()

    plt.savefig(buffer, format="png")
    plt.close()

    buffer.seek(0)

    return StreamingResponse(buffer, media_type="image/png")



# Dashboard Summary Endpoint

@app.get("/dashboard-summary", response_model=DashboardSummaryResponse, tags=["Analytics"])
def dashboard_summary():

    if df.empty:
        return {"error": "Dataset not loaded"}

    total_revenue = float(df["revenue"].sum())
    total_orders = int(len(df))

    top_category = (
        df.groupby("product_category")["revenue"]
        .sum()
        .sort_values(ascending=False)
        .index[0]
    )

    avg_rating = float(df["rating"].mean())

    return {
        "total_revenue": total_revenue,
        "total_orders": total_orders,
        "top_category": top_category,
        "average_rating": avg_rating
    }

# -----------------------------
# Health Check Endpoint
# -----------------------------

@app.get("/health", tags=["System"])
def health_check():
    return {"status": "API running", "service": "ecommerce-analytics"}