import streamlit as st
import numpy as np

from helper import (
    load_models,
    cluster_name,
    cluster_action
)

# -----------------------------------------
# Load ML Models
# -----------------------------------------

model, scaler, _ = load_models()


def show_segmentation():

    st.title("👥 Customer Segmentation")

    st.markdown("""
Predict the customer segment using **Recency, Frequency and Monetary (RFM)** values.
""")

    st.divider()

    st.subheader("Enter Customer Details")

    col1, col2, col3 = st.columns(3)

    with col1:

        recency = st.number_input(
            "Recency (Days)",
            min_value=0,
            value=30,
            step=1
        )

    with col2:

        frequency = st.number_input(
            "Frequency",
            min_value=1,
            value=5,
            step=1
        )

    with col3:

        monetary = st.number_input(
            "Monetary",
            min_value=0.0,
            value=1000.0,
            step=100.0
        )

    st.divider()
    # -----------------------------------------
# Predict Button
# -----------------------------------------

if st.button(
    "🔍 Predict Customer Segment",
    use_container_width=True
):

    try:

        # Create Feature Array
        customer = np.array(
            [[recency, frequency, monetary]]
        )

        # Scale Features
        customer_scaled = scaler.transform(
            customer
        )

        # Predict Cluster
        cluster = model.predict(
            customer_scaled
        )[0]

        customer_type = cluster_name(cluster)

        actions = cluster_action(cluster)

        st.success(
            f"Predicted Segment : {customer_type}"
        )

        st.divider()

        st.subheader("📈 Business Recommendation")

        for action in actions:

            st.markdown(
                f"✅ {action}"
            )

    except Exception as e:

        st.error(e)

        st.divider()

with st.expander(
    "ℹ Interpretation of Customer Segments"
):

    st.markdown("""
### ⭐ High Value Customer

- High purchase frequency
- Very high spending
- Recently active

**Business Strategy**

- Premium membership
- VIP rewards
- Exclusive offers

---

### 🟢 Loyal Customer

- Regular purchases
- Good revenue

**Business Strategy**

- Cross-selling
- Product bundles
- Loyalty points

---

### 🟡 Occasional Customer

- Purchases occasionally
- Moderate spending

**Business Strategy**

- Email marketing
- Seasonal discounts

---

### 🔴 At Risk Customer

- Long time since last purchase
- Low purchase frequency

**Business Strategy**

- Win-back campaign
- Discount coupons
- Reactivation emails
""")