import pandas as pd

# Load raw scraped data
df = pd.read_csv("mclaren_mcl38_raw.csv")

# Fix the misplaced specification
df.loc[df["Specification"].isna(), "Specification"] = "Max rpm Exhaust Turbine"
df.loc[df["Specification"] == "Max rpm Exhaust Turbine", "Value"] = "125,000 rpm"

# Remove section headings
section_headings = [
    "CHASSIS",
    "ENERGY RECOVERY SYSTEM",
    "LOGISTICS"
]

df = df[~df["Specification"].isin(section_headings)]

# Reset row numbers
df = df.reset_index(drop=True)

# Save cleaned dataset
df.to_csv("mclaren_mcl38_cleaned.csv", index=False)

print("Cleaning completed!")
print("Rows:", len(df))
print("Columns:", len(df.columns))

print("\nMissing values after cleaning:")
print(df.isnull().sum())

print("\nCleaned data:")
print(df.to_string(index=False))