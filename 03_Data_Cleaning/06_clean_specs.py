import pandas as pd

# Load raw scraped data
df = pd.read_csv("f1_specs_raw.csv")

print("Before cleaning:")
print("Rows:", len(df))

# Remove rows where Value is missing
df = df.dropna(subset=["Value"])

# Remove rows where Value is empty
df = df[
    df["Value"].astype(str).str.strip() != ""
]

print("\nAfter removing empty values:")
print("Rows:", len(df))

print("\nFirst 10 rows:")
print(df.head(10).to_string(index=False))

# Save cleaned data
df.to_csv(
    "f1_specs_cleaned.csv",
    index=False
)

print("\nCleaned data saved successfully!")
print("File: f1_specs_cleaned.csv")