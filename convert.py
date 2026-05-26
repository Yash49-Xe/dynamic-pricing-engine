import pandas as pd

# 1. Load the old CSV
print("Loading CSV...")
df = pd.read_csv("inventory.csv")

# 2. Save it as a Parquet file
print("Converting to Parquet...")
df.to_parquet("inventory.parquet", engine="pyarrow")

print("Conversion complete! You can now delete convert.py")