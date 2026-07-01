import os
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler


class RFMAnalysis:

    def __init__(self, file_path):

        self.df = pd.read_csv(file_path)

        self.df["InvoiceDate"] = pd.to_datetime(
            self.df["InvoiceDate"]
        )

        os.makedirs("data/processed", exist_ok=True)
        os.makedirs("outputs/figures", exist_ok=True)

    def create_rfm(self):

        snapshot_date = self.df["InvoiceDate"].max() + pd.Timedelta(days=1)

        self.rfm = (
            self.df
            .groupby("CustomerID")
            .agg(
                Recency=("InvoiceDate",
                         lambda x: (snapshot_date - x.max()).days),
                Frequency=("InvoiceNo", "nunique"),
                Monetary=("TotalAmount", "sum")
            )
            .reset_index()
        )

        print("\nRFM Table Created Successfully\n")
        print(self.rfm.head())

    def save_rfm(self):

        self.rfm.to_csv(
            "data/processed/rfm_table.csv",
            index=False
        )

        print("\nRFM table saved.")

    def scale_features(self):

        scaler = StandardScaler()

        scaled = scaler.fit_transform(
            self.rfm[["Recency", "Frequency", "Monetary"]]
        )

        self.scaled_rfm = pd.DataFrame(
            scaled,
            columns=[
                "Recency",
                "Frequency",
                "Monetary"
            ]
        )

        self.scaled_rfm.to_csv(
            "data/processed/rfm_scaled.csv",
            index=False
        )

        print("Scaled RFM saved.")

    def distributions(self):

        columns = [
            "Recency",
            "Frequency",
            "Monetary"
        ]

        for col in columns:

            plt.figure(figsize=(8,5))

            plt.hist(
                self.rfm[col],
                bins=40
            )

            plt.title(f"{col} Distribution")

            plt.tight_layout()

            plt.savefig(
                f"outputs/figures/{col.lower()}_distribution.png"
            )

            plt.show()

    def summary(self):

        print("\n")
        print(self.rfm.describe())

    def run(self):

        self.create_rfm()

        self.summary()

        self.distributions()

        self.scale_features()

        self.save_rfm()


if __name__ == "__main__":

    analysis = RFMAnalysis(
        "data/processed/cleaned_online_retail.csv"
    )

    analysis.run()