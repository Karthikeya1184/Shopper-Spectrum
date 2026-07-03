import streamlit as st
import pandas as pd

from dashboard import show_dashboard
from segmentation import show_segmentation
from recommendation_page import show_recommendation
from about import show_about

# -----------------------------
# PAGE CONFIG
# -----------------------------
st.set_page_config(
    page_title="Shopper Spectrum",
    page_icon="🛒",
    layout="wide"
)

# -----------------------------
# LOAD DATA
# -----------------------------
@st.cache_data
def load_data():
    return pd.read_csv("data/processed/cleaned_online_retail.csv")

df = load_data()

# -----------------------------
# KPIs
# -----------------------------
total_revenue = df["TotalAmount"].sum()
total_customers = df["CustomerID"].nunique()
total_products = df["Description"].nunique()
total_countries = df["Country"].nunique()

# -----------------------------
# HEADER
# -----------------------------
st.title("🛒 Shopper Spectrum")

st.caption(
    "Customer Segmentation & Product Recommendation Dashboard"
)

st.divider()

# -----------------------------
# KPI CARDS
# -----------------------------
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "💰 Revenue",
        f"₹{total_revenue:,.0f}"
    )

with col2:
    st.metric(
        "👥 Customers",
        f"{total_customers:,}"
    )

with col3:
    st.metric(
        "📦 Products",
        f"{total_products:,}"
    )

with col4:
    st.metric(
        "🌍 Countries",
        f"{total_countries}"
    )

st.divider()

# -----------------------------
# TABS
# -----------------------------
home, dashboard, segmentation, recommendation, about = st.tabs(
    [
        "🏠 Home",
        "📊 Dashboard",
        "👥 Customer Segmentation",
        "🛍 Recommendation",
        "ℹ About"
    ]
)

# ==========================================================
# HOME TAB
# ==========================================================

with home:

    st.title("🛒 Shopper Spectrum")

    st.subheader("Customer Analytics & Product Recommendation System")

    st.markdown("---")

    st.markdown("""
### 🎯 Project Objective

Shopper Spectrum is an end-to-end customer analytics platform built using
Machine Learning and Streamlit.

The project helps businesses:

- 📈 Increase Sales
- 👥 Understand Customer Behaviour
- 🎯 Improve Marketing Campaigns
- 🛍 Recommend Similar Products
- 💰 Increase Customer Lifetime Value
""")

    st.markdown("---")

    col1, col2 = st.columns(2)

    with col1:

        st.success("""
### 🔍 Features

✔ Exploratory Data Analysis

✔ Customer Segmentation

✔ Product Recommendation

✔ Business Insights

✔ Interactive Dashboard
""")

    with col2:

        st.info("""
### 🤖 Machine Learning

• K-Means Clustering

• Cosine Similarity

• RFM Analysis

• Feature Engineering
""")

    st.markdown("---")

    st.header("📌 Project Workflow")

    st.code("""
Online Retail Dataset
        │
        ▼
Data Cleaning
        │
        ▼
Exploratory Data Analysis
        │
        ▼
Feature Engineering
        │
        ▼
RFM Analysis
        │
        ▼
Customer Segmentation
        │
        ▼
Product Recommendation
        │
        ▼
Business Dashboard
""")

    st.markdown("---")

    st.success("🚀 Navigate using the tabs above to explore the project.")

# ==========================================================
# DASHBOARD TAB
# ==========================================================

with dashboard:
    show_dashboard()

# ==========================================================
# CUSTOMER SEGMENTATION TAB
# ==========================================================

with segmentation:
    show_segmentation()

# ==========================================================
# RECOMMENDATION TAB
# ==========================================================

with recommendation:
    show_recommendation()

# ==========================================================
# ABOUT TAB
# ==========================================================

with about:
    show_about()