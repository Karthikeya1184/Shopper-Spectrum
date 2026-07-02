# 🛒 Shopper Spectrum: Customer Segmentation & Product Recommendation in E-Commerce

## 📖 Project Overview

Shopper Spectrum is an end-to-end Data Analytics and Machine Learning project that analyzes online retail transaction data to understand customer purchasing behavior, segment customers using RFM analysis and KMeans clustering, and recommend products using Item-Based Collaborative Filtering.

This project demonstrates the complete data analytics lifecycle—from data preprocessing and exploratory analysis to machine learning and deployment using Streamlit.

---

## 🎯 Business Objective

The project helps an e-commerce business answer questions such as:

- Who are the most valuable customers?
- Which customers are likely to churn?
- Which products generate the highest revenue?
- Which products are frequently purchased together?
- How can personalized recommendations improve customer experience?

---

## 🛠️ Tech Stack

- Python
- Pandas
- NumPy
- Matplotlib
- Scikit-learn
- Joblib
- Streamlit
- Jupyter Notebook
- Git & GitHub

---

## 📂 Project Structure

```text
Shopper-Spectrum/
│
├── data/
│   ├── raw/
│   └── processed/
│
├── models/
│
├── notebooks/
│
├── outputs/
│   ├── figures/
│   ├── reports/
│   └── tables/
│
├── src/
│   ├── load_data.py
│   ├── data_cleaning.py
│   ├── eda.py
│   ├── rfm.py
│   ├── clustering.py
│   ├── recommendation.py
│   └── utils.py
│
├── streamlit_app/
│   └── app.py
│
├── README.md
├── requirements.txt
└── .gitignore
```

---

# 📊 Dataset

Dataset: Online Retail Transactions

Columns:

- InvoiceNo
- StockCode
- Description
- Quantity
- InvoiceDate
- UnitPrice
- CustomerID
- Country

---

# ✅ Project Workflow

```
Business Understanding
        ↓
Dataset Loading
        ↓
Data Cleaning
        ↓
Exploratory Data Analysis
        ↓
RFM Analysis
        ↓
Customer Segmentation
        ↓
Product Recommendation
        ↓
Streamlit Dashboard
```

---

# 📈 Current Progress

| Module | Status |
|---------|--------|
| Project Setup | ✅ |
| Data Cleaning | ✅ |
| Exploratory Data Analysis | ✅ |
| RFM Analysis | ✅ |
| Customer Segmentation | ✅ |
| Product Recommendation | ⏳ |
| Streamlit App | ⏳ |
| Documentation | ⏳ |
---

# 📊 Exploratory Data Analysis

Completed analyses include:

- Revenue Analysis
- Country-wise Sales
- Monthly Sales Trend
- Daily Sales Trend
- Top Customers
- Top Selling Products
- Top Revenue Products
- Purchase Distribution

Generated charts are saved in:

outputs/figures/

---

# 📌 RFM Analysis

Features created:

- Recency
- Frequency
- Monetary

Output files:

- rfm_table.csv
- rfm_scaled.csv

---

# 🚀 Future Work

# 🤖 Machine Learning

## Customer Segmentation

Implemented **KMeans Clustering** using RFM (Recency, Frequency, Monetary) features.

### Machine Learning Workflow

- Feature Engineering using RFM Analysis
- Feature Scaling using StandardScaler
- Elbow Method for cluster selection
- Silhouette Score evaluation
- KMeans Clustering
- Customer Segment Generation
- Model Persistence using Joblib

### Generated Files

```
models/
│
├── kmeans_model.pkl
└── scaler.pkl
```

```
data/processed/
│
└── customer_segments.csv
```

```
outputs/
├── figures/
│   ├── elbow_curve.png
│   └── customer_clusters.png
│
└── tables/
    └── cluster_summary.csv
```

---

# 🚀 Remaining Modules

- Product Recommendation System
- Streamlit Dashboard
- Final Documentation
- GitHub Project Polishing
---

# 👨‍💻 Author

**Karthikeya Bammidi**

MBA – SRM University

Aspiring Business Analyst | Data Analyst

GitHub: *(Add your GitHub profile link here)*

LinkedIn: *(Add your LinkedIn profile link here)*

---

# ⭐ Acknowledgements

This project was developed for learning Customer Analytics, Customer Segmentation, and Recommendation Systems using Python and Machine Learning.