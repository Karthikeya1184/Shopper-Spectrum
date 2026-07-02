import os
import joblib
import pandas as pd

from sklearn.metrics.pairwise import cosine_similarity


class ProductRecommendation:

    def __init__(self):

        self.df = pd.read_csv(
            "data/processed/cleaned_online_retail.csv"
        )

        os.makedirs("models", exist_ok=True)

    def create_matrix(self):

        self.matrix = self.df.pivot_table(
            index="CustomerID",
            columns="Description",
            values="Quantity",
            aggfunc="sum",
            fill_value=0
        )

        print("\nCustomer-Product Matrix Created")
        print(self.matrix.shape)

    def compute_similarity(self):

        similarity = cosine_similarity(
            self.matrix.T
        )

        self.similarity_df = pd.DataFrame(
            similarity,
            index=self.matrix.columns,
            columns=self.matrix.columns
        )

        print("\nSimilarity Matrix Created")

    def save_similarity(self):

        joblib.dump(
            self.similarity_df,
            "models/product_similarity.pkl"
        )

        print("\nSimilarity Model Saved")

    def save_product_list(self):

        products = pd.DataFrame(
            self.matrix.columns,
            columns=["Product"]
        )

        products.to_csv(
            "data/processed/product_list.csv",
            index=False
        )

        print("Product List Saved")

    def recommend(self, product_name, top_n=5):

        if product_name not in self.similarity_df.index:
            return []

        recommendations = (
            self.similarity_df[product_name]
            .sort_values(ascending=False)
            .iloc[1:top_n + 1]
        )

        return recommendations.index.tolist()

    def test(self):

        product = self.matrix.columns[0]

        print("\nSample Product")
        print(product)

        print("\nRecommendations")
        print(self.recommend(product))

    def run(self):

        self.create_matrix()

        self.compute_similarity()

        self.save_similarity()

        self.save_product_list()

        self.test()


if __name__ == "__main__":

    recommendation = ProductRecommendation()

    recommendation.run()