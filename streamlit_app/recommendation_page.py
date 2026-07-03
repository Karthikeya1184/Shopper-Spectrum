import streamlit as st
from helper import load_models
def show_recommendation():

    # Load model INSIDE the function
    _, _, similarity_df = load_models()

    products = similarity_df.index.astype(str).tolist()

    st.title("🛍 Product Recommendation System")

    st.write("Similarity Shape:", similarity_df.shape)
    st.write("Products:", len(products))

    st.divider()

    selected_product = st.selectbox(
        "Select a Product",
        options=products,
        index=None,
        placeholder="Choose a product..."
    )

    if selected_product is None:
        return

    if st.button("🔍 Get Recommendations", use_container_width=True):

        recommendations = (
            similarity_df.loc[selected_product]
            .sort_values(ascending=False)
            .iloc[1:6]
        )

        st.success(f"Recommendations for **{selected_product}**")

        for i, item in enumerate(recommendations.index, 1):
            st.info(f"{i}. {item}")