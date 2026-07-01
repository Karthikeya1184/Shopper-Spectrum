import pandas as pd


class DataCleaner:
    """
    A class for cleaning the Online Retail dataset.
    """

    def __init__(self, file_path):
        self.file_path = file_path
        self.df = None

    def load_data(self):
        """
        Load dataset.
        """
        self.df = pd.read_csv(
            self.file_path,
            encoding="ISO-8859-1"
        )

        print("Dataset loaded successfully.")
        print("-" * 50)

    def dataset_summary(self):

        print("Dataset Shape:", self.df.shape)

        print("\nMissing Values")

        print(self.df.isnull().sum())

        print("\nDuplicate Rows:", self.df.duplicated().sum())

    def remove_missing_customer(self):

        before = len(self.df)

        self.df = self.df.dropna(subset=["CustomerID"])

        after = len(self.df)

        print(f"Removed {before-after} rows with missing CustomerID")

    def remove_duplicates(self):

        before = len(self.df)

        self.df = self.df.drop_duplicates()

        after = len(self.df)

        print(f"Removed {before-after} duplicate rows")

    def remove_cancelled_orders(self):

        before = len(self.df)

        self.df = self.df[
            ~self.df["InvoiceNo"].astype(str).str.startswith("C")
        ]

        after = len(self.df)

        print(f"Removed {before-after} cancelled orders")

    def remove_invalid_values(self):

        before = len(self.df)

        self.df = self.df[
            (self.df["Quantity"] > 0)
            &
            (self.df["UnitPrice"] > 0)
        ]

        after = len(self.df)

        print(f"Removed {before-after} invalid rows")

    def convert_date(self):

        self.df["InvoiceDate"] = pd.to_datetime(
            self.df["InvoiceDate"]
        )

        print("InvoiceDate converted successfully")

    def create_total_amount(self):

        self.df["TotalAmount"] = (
            self.df["Quantity"]
            *
            self.df["UnitPrice"]
        )

        print("TotalAmount column created")

    def final_summary(self):

        print("\n")
        print("=" * 50)

        print("Final Dataset Shape")

        print(self.df.shape)

        print("=" * 50)

    def save_dataset(self):

        output_path = "data/processed/cleaned_online_retail.csv"

        self.df.to_csv(
            output_path,
            index=False
        )

        print("Cleaned dataset saved successfully")

    def clean(self):

        self.load_data()

        self.dataset_summary()

        self.remove_missing_customer()

        self.remove_duplicates()

        self.remove_cancelled_orders()

        self.remove_invalid_values()

        self.convert_date()

        self.create_total_amount()

        self.final_summary()

        self.save_dataset()


if __name__ == "__main__":

    cleaner = DataCleaner(
        "data/raw/online_retail.csv"
    )

    cleaner.clean()