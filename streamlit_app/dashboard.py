import streamlit as st
from pathlib import Path
import pandas as pd

# ----------------------------------------------------
# Project Paths
# ----------------------------------------------------

ROOT = Path(__file__).resolve().parent.parent

FIGURES = ROOT / "outputs" / "figures"
DATA = ROOT / "data" / "processed" / "cleaned_online_retail.csv"


# ----------------------------------------------------
# Load Dataset
# ----------------------------------------------------

@st.cache_data
def load_data():
    return pd.read_csv(DATA)


# ----------------------------------------------------
# Display Image
# ----------------------------------------------------

def image_card(title, filename):

    st.subheader(title)

    image_path = FIGURES / filename

    if image_path.exists():

        st.image(
            str(image_path),
            use_container_width=True
        )

    else:

        st.warning(f"Image not found:\n{image_path}")


# ----------------------------------------------------
# Dashboard
# ----------------------------------------------------

def show_dashboard():

    df = load_data()

    st.title("📊 Sales Analytics Dashboard")

    st.caption(
        "Exploratory Data Analysis of the Online Retail Dataset"
    )

    st.divider()

    # ----------------------------------------------------
    # KPI CARDS
    # ----------------------------------------------------

    revenue = df["TotalAmount"].sum()
    customers = df["CustomerID"].nunique()
    products = df["Description"].nunique()
    countries = df["Country"].nunique()

    col1, col2, col3, col4 = st.columns(4)

    col1.metric(
        "💰 Revenue",
        f"₹{revenue:,.0f}"
    )

    col2.metric(
        "👥 Customers",
        customers
    )

    col3.metric(
        "📦 Products",
        products
    )

    col4.metric(
        "🌍 Countries",
        countries
    )

    st.divider()

    # ----------------------------------------------------
    # SALES
    # ----------------------------------------------------

    st.header("📈 Sales Overview")

    c1, c2 = st.columns(2)

    with c1:
        image_card(
            "Monthly Sales",
            "monthly_sales.png"
        )

    with c2:
        image_card(
            "Daily Sales",
            "daily_sales.png"
        )

    st.divider()

    # ----------------------------------------------------
    # COUNTRY
    # ----------------------------------------------------

    st.header("🌍 Country Analysis")

    image_card(
        "Country Sales",
        "country_sales.png"
    )

    st.divider()

    # ----------------------------------------------------
    # PRODUCT
    # ----------------------------------------------------

    st.header("📦 Product Analysis")

    c1, c2 = st.columns(2)

    with c1:
        image_card(
            "Top Selling Products",
            "top_selling_products.png"
        )

    with c2:
        image_card(
            "Top Revenue Products",
            "top_revenue_products.png"
        )

    st.divider()

    # ----------------------------------------------------
    # CUSTOMER
    # ----------------------------------------------------

    st.header("👥 Customer Analysis")

    c1, c2 = st.columns(2)

    with c1:
        image_card(
            "Top Customers",
            "top_customers.png"
        )

    with c2:
        image_card(
            "Purchase Distribution",
            "purchase_distribution.png"
        )

    st.divider()

    # ----------------------------------------------------
    # RFM
    # ----------------------------------------------------

    st.header("📊 RFM Analysis")

    c1, c2 = st.columns(2)

    with c1:
        image_card(
            "Recency Distribution",
            "recency_distribution.png"
        )

    with c2:
        image_card(
            "Frequency Distribution",
            "frequency_distribution.png"
        )

    c3, c4 = st.columns(2)

    with c3:
        image_card(
            "Monetary Distribution",
            "monetary_distribution.png"
        )

    with c4:
        image_card(
            "Customer Clusters",
            "customer_clusters.png"
        )

    st.divider()

    # ----------------------------------------------------
    # DATA PREVIEW
    # ----------------------------------------------------

    with st.expander("📄 View Dataset"):

        st.dataframe(
            df.head(20),
            use_container_width=True
        )

    st.divider()

    # ----------------------------------------------------
    # BUSINESS INSIGHTS
    # ----------------------------------------------------

    st.header("💡 Business Insights")

    st.success("""
### Key Findings

✅ Revenue is concentrated among a small percentage of customers.

✅ High-value customers contribute the majority of total sales.

✅ Product recommendation can improve cross-selling opportunities.

✅ Customer segmentation helps identify loyal and at-risk customers.

✅ RFM analysis supports targeted marketing campaigns.
""")