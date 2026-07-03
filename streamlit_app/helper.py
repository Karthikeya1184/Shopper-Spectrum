import pandas as pd
import joblib
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

DATA_DIR = ROOT / "data" / "processed"
MODEL_DIR = ROOT / "models"
FIGURE_DIR = ROOT / "outputs" / "figures"


def load_data():
    return pd.read_csv(DATA_DIR / "cleaned_online_retail.csv")


def load_transactions():
    return load_data()


def load_segments():
    return pd.read_csv(DATA_DIR / "customer_segments.csv")


def load_products():
    return pd.read_csv(DATA_DIR / "product_list.csv")


def load_models():
    model = joblib.load(MODEL_DIR / "kmeans_model.pkl")
    scaler = joblib.load(MODEL_DIR / "scaler.pkl")
    similarity = joblib.load(MODEL_DIR / "product_similarity.pkl")

    print("=" * 50)
    print("Similarity Shape:", similarity.shape)
    print("Index Length:", len(similarity.index))
    print("First 5 Products:", list(similarity.index[:5]))
    print("=" * 50)

    return model, scaler, similarity

def calculate_kpis(df):
    revenue = df["TotalAmount"].sum()
    customers = df["CustomerID"].nunique()
    products = df["Description"].nunique()
    countries = df["Country"].nunique()
    return revenue, customers, products, countries


def get_kpis(df):
    return {
        "Revenue": df["TotalAmount"].sum(),
        "Customers": df["CustomerID"].nunique(),
        "Products": df["Description"].nunique(),
        "Countries": df["Country"].nunique(),
    }


def cluster_name(cluster_id):
    mapping = {
        2: "⭐ High Value Customer",
        3: "🟢 Loyal Customer",
        0: "🟡 Occasional Customer",
        1: "🔴 At Risk Customer",
    }
    return mapping.get(cluster_id, "Unknown Customer")


def cluster_action(cluster_id):
    actions = {
        2: [
            "Provide Premium Membership",
            "Offer Exclusive Discounts",
            "Reward Loyalty with VIP Benefits",
        ],
        3: [
            "Encourage Repeat Purchases",
            "Recommend Complementary Products",
            "Offer Bundle Discounts",
        ],
        0: [
            "Send Promotional Emails",
            "Offer Seasonal Discounts",
            "Increase Customer Engagement",
        ],
        1: [
            "Launch Win-Back Campaign",
            "Provide Special Coupons",
            "Send Reactivation Emails",
        ],
    }

    return actions.get(cluster_id, [])