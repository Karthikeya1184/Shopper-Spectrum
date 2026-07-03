from pathlib import Path
import joblib
import pandas as pd

ROOT = Path(__file__).resolve().parent.parent

model_path = ROOT / "models" / "product_similarity.pkl"

print("Loading from:")
print(model_path)

similarity = joblib.load(model_path)

print("\nType:", type(similarity))
print("Shape:", similarity.shape)
print("Index length:", len(similarity.index))

if len(similarity.index) > 0:
    print("\nFirst 5 products:")
    print(similarity.index[:5])

products = pd.DataFrame(
    {"Product": similarity.index.tolist()}
)

print("\nGenerated product list:")
print(products.head())
print(products.shape)

output_path = ROOT / "data" / "processed" / "product_list.csv"
products.to_csv(output_path, index=False)

print("\nSaved to:")
print(output_path)