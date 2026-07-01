import os
import pandas as pd
import matplotlib.pyplot as plt


class EDA:

    def __init__(self, file_path):

        self.df = pd.read_csv(file_path)

        self.df["InvoiceDate"] = pd.to_datetime(self.df["InvoiceDate"])

        os.makedirs("outputs/figures", exist_ok=True)

    def revenue_summary(self):

        revenue = self.df["TotalAmount"].sum()

        print("=" * 50)
        print("TOTAL REVENUE")
        print(f"₹ {revenue:,.2f}")
        print("=" * 50)

    def top_products_quantity(self):

        top = (
            self.df
            .groupby("Description")["Quantity"]
            .sum()
            .sort_values(ascending=False)
            .head(10)
        )

        plt.figure(figsize=(12,6))
        top.sort_values().plot(kind="barh")
        plt.title("Top Selling Products")
        plt.xlabel("Quantity Sold")
        plt.tight_layout()

        plt.savefig(
            "outputs/figures/top_selling_products.png"
        )

        plt.show()

    def top_products_revenue(self):

        top = (
            self.df
            .groupby("Description")["TotalAmount"]
            .sum()
            .sort_values(ascending=False)
            .head(10)
        )

        plt.figure(figsize=(12,6))
        top.sort_values().plot(kind="barh")
        plt.title("Top Revenue Products")
        plt.xlabel("Revenue")
        plt.tight_layout()

        plt.savefig(
            "outputs/figures/top_revenue_products.png"
        )

        plt.show()

    def country_sales(self):

        sales = (
            self.df
            .groupby("Country")["TotalAmount"]
            .sum()
            .sort_values(ascending=False)
            .head(10)
        )

        plt.figure(figsize=(12,6))
        sales.sort_values().plot(kind="barh")
        plt.title("Top Countries by Revenue")
        plt.xlabel("Revenue")
        plt.tight_layout()

        plt.savefig(
            "outputs/figures/country_sales.png"
        )

        plt.show()

    def monthly_sales(self):

        monthly = (
            self.df
            .set_index("InvoiceDate")
            .resample("ME")["TotalAmount"]
            .sum()
        )

        plt.figure(figsize=(14,6))

        monthly.plot(marker="o")

        plt.title("Monthly Revenue Trend")

        plt.ylabel("Revenue")

        plt.tight_layout()

        plt.savefig(
            "outputs/figures/monthly_sales.png"
        )

        plt.show()

    def daily_sales(self):

        daily = (
            self.df
            .set_index("InvoiceDate")
            .resample("D")["TotalAmount"]
            .sum()
        )

        plt.figure(figsize=(14,6))

        daily.plot()

        plt.title("Daily Revenue")

        plt.tight_layout()

        plt.savefig(
            "outputs/figures/daily_sales.png"
        )

        plt.show()

    def top_customers(self):

        top = (
            self.df
            .groupby("CustomerID")["TotalAmount"]
            .sum()
            .sort_values(ascending=False)
            .head(10)
        )

        plt.figure(figsize=(12,6))

        top.sort_values().plot(kind="barh")

        plt.title("Top Customers")

        plt.xlabel("Revenue")

        plt.tight_layout()

        plt.savefig(
            "outputs/figures/top_customers.png"
        )

        plt.show()

    def purchase_distribution(self):

        plt.figure(figsize=(8,6))

        plt.hist(
            self.df["TotalAmount"],
            bins=50
        )

        plt.title("Purchase Amount Distribution")

        plt.xlabel("Purchase Amount")

        plt.ylabel("Frequency")

        plt.tight_layout()

        plt.savefig(
            "outputs/figures/purchase_distribution.png"
        )

        plt.show()

    def run(self):

        self.revenue_summary()

        self.top_products_quantity()

        self.top_products_revenue()

        self.country_sales()

        self.monthly_sales()

        self.daily_sales()

        self.top_customers()

        self.purchase_distribution()


if __name__ == "__main__":

    eda = EDA(
        "data/processed/cleaned_online_retail.csv"
    )

    eda.run()