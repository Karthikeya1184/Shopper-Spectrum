import streamlit as st


def show_about():

    st.title("ℹ About Shopper Spectrum")

    st.markdown("---")

    st.header("📌 Project Overview")

    st.write("""
Shopper Spectrum is a Customer Analytics and Product Recommendation System
developed using the Online Retail Dataset.

The project combines Exploratory Data Analysis (EDA),
Customer Segmentation using Machine Learning,
and a Product Recommendation System to help businesses
understand customer purchasing behaviour and improve marketing strategies.
""")

    st.markdown("---")

    st.header("🎯 Objectives")

    st.markdown("""
- Perform Exploratory Data Analysis
- Identify customer purchasing behaviour
- Segment customers using RFM Analysis
- Build Customer Segmentation using K-Means Clustering
- Recommend similar products using Cosine Similarity
- Visualize business insights using Streamlit
""")

    st.markdown("---")

    st.header("🛠 Technology Stack")

    col1, col2 = st.columns(2)

    with col1:

        st.markdown("""
### Programming

- Python
- Pandas
- NumPy
- Matplotlib
- Plotly
        """)

    with col2:

        st.markdown("""
### Machine Learning

- Scikit-Learn
- K-Means Clustering
- Cosine Similarity
- Joblib
- Streamlit
        """)

    st.markdown("---")

    st.header("📂 Project Workflow")

    st.markdown("""
Dataset

⬇

Data Cleaning

⬇

Exploratory Data Analysis

⬇

Feature Engineering

⬇

RFM Analysis

⬇

Customer Segmentation

⬇

Product Recommendation

⬇

Interactive Streamlit Dashboard
""")

    st.markdown("---")

    st.header("📈 Machine Learning Models")

    st.success("""
✔ Customer Segmentation

Model Used:
K-Means Clustering

Purpose:
Group customers into meaningful business segments.
""")

    st.success("""
✔ Product Recommendation

Algorithm:
Cosine Similarity

Purpose:
Recommend products similar to customer interests.
""")

    st.markdown("---")

    st.header("👨‍💻 Developer")

    st.write("""
**Karthikeya Bammidi**

MBA Business Analytics

SRM Institute of Science and Technology
""")

    st.markdown("---")

    st.header("🚀 Future Enhancements")

    st.markdown("""
- Deploy on Streamlit Cloud
- Add Login Authentication
- Add Customer Lifetime Value Prediction
- Build Real-Time Recommendation Engine
- Deploy using Docker
""")