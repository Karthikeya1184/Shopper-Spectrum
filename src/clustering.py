import os
import joblib
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
from sklearn.preprocessing import StandardScaler

class CustomerSegmentation:

    def __init__(self):

        self.rfm = pd.read_csv(
            "data/processed/rfm_table.csv"
        )

        os.makedirs("models", exist_ok=True)
        os.makedirs("outputs/figures", exist_ok=True)

    def scale_data(self):

        scaler = StandardScaler()

        self.scaled_data = scaler.fit_transform(

            self.rfm[
                ["Recency",
                 "Frequency",
                 "Monetary"]
            ]
        )

        joblib.dump(
            scaler,
            "models/scaler.pkl"
        )

        print("Scaler Saved")


    def elbow_method(self):

        inertia = []

        k_values = range(2,11)

        for k in k_values:

            model = KMeans(

                n_clusters=k,

                random_state=42,

                n_init=10

            )

            model.fit(self.scaled_data)

            inertia.append(model.inertia_)

        plt.figure(figsize=(8,5))

        plt.plot(

            k_values,

            inertia,

            marker="o"

        )

        plt.title("Elbow Method")

        plt.xlabel("Number of Clusters")

        plt.ylabel("Inertia")

        plt.grid(True)

        plt.savefig(

            "outputs/figures/elbow_curve.png"

        )

        plt.show()


    def silhouette_analysis(self):

        print()

        print("Silhouette Scores")

        print("-"*40)

        for k in range(2,11):

            model = KMeans(

                n_clusters=k,

                random_state=42,

                n_init=10

            )

            labels = model.fit_predict(

                self.scaled_data

            )

            score = silhouette_score(

                self.scaled_data,

                labels

            )

            print(f"K={k} : {score:.4f}")


    def train_model(self):

        self.model = KMeans(
            n_clusters=4,
            random_state=42,
            n_init=10
        )

        self.rfm["Cluster"] = self.model.fit_predict(
            self.scaled_data
        )

        joblib.dump(
            self.model,
            "models/kmeans_model.pkl"
        )

        print("\nKMeans Model Saved Successfully.")


    def cluster_summary(self):

        summary = (
            self.rfm
            .groupby("Cluster")[["Recency",
                                 "Frequency",
                                 "Monetary"]]
            .mean()
        )

        print("\nCluster Summary")
        print("="*50)
        print(summary)

        summary.to_csv(
            "outputs/tables/cluster_summary.csv"
        )


    def visualize_clusters(self):

        plt.figure(figsize=(10,7))

        plt.scatter(

            self.rfm["Frequency"],

            self.rfm["Monetary"],

            c=self.rfm["Cluster"]

        )

        plt.title("Customer Segments")

        plt.xlabel("Frequency")

        plt.ylabel("Monetary")

        plt.savefig(
            "outputs/figures/customer_clusters.png"
        )

        plt.show()


    def save_segments(self):

        self.rfm.to_csv(

            "data/processed/customer_segments.csv",

            index=False

        )

        print("\nCustomer Segments Saved.")


    def run(self):

        self.scale_data()

        self.elbow_method()

        self.silhouette_analysis()

        self.train_model()

        self.cluster_summary()

        self.visualize_clusters()

        self.save_segments()


if __name__ == "__main__":

    segmentation = CustomerSegmentation()

    segmentation.run()