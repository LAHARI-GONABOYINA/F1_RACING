import pandas as pd


# ==========================================
# Load cleaned data from Step 1
# ==========================================

df = pd.read_csv("f1_specs_cleaned.csv")

print("Before text cleaning:")
print("Rows:", len(df))
print("Columns:", len(df.columns))


# ==========================================
# Clean Specification column
# ==========================================

df["Specification"] = (
    df["Specification"]
    .astype(str)
    .str.replace(r"\s+", " ", regex=True)
    .str.strip()
)


# ==========================================
# Clean Value column
# ==========================================

df["Value"] = (
    df["Value"]
    .astype(str)
    .str.replace(r"\s+", " ", regex=True)
    .str.strip()
)


# ==========================================
# Display cleaned data
# ==========================================

print("\nAfter text cleaning:")

print(
    df.head(10).to_string(index=False)
)


# ==========================================
# Check for unwanted formatting
# ==========================================

print("\nChecking text formatting...")

print(
    "Specification values with extra whitespace:",
    df["Specification"].str.contains(
        r"\s{2,}",
        regex=True
    ).sum()
)

print(
    "Value entries with extra whitespace:",
    df["Value"].str.contains(
        r"\s{2,}",
        regex=True
    ).sum()
)


# ==========================================
# Save cleaned dataset
# ==========================================

df.to_csv(
    "f1_specs_cleaned_text.csv",
    index=False
)


print("\n================================")
print("TEXT CLEANING COMPLETED")
print("================================")

print("Rows:", len(df))
print("Columns:", len(df.columns))

print(
    "\nFile saved:",
    "f1_specs_cleaned_text.csv"
)