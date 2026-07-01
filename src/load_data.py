import pandas as pd


def load_dataset(file_path):
    """
    Load the Online Retail dataset.
    """
    try:
        df = pd.read_csv(file_path, encoding="ISO-8859-1")
        print("Dataset loaded successfully.")
        return df

    except FileNotFoundError:
        print("File not found.")
        return None

    except Exception as e:
        print("Error:", e)
        return None


if __name__ == "__main__":

    path = "data/raw/online_retail.csv"

    df = load_dataset(path)

    if df is not None:

        print("\nFirst Five Rows\n")
        print(df.head())

        print("\nDataset Shape")
        print(df.shape)

        print("\nColumns")
        print(df.columns)

        print("\nData Types")
        print(df.dtypes)