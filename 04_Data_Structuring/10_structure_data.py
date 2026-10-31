import pandas as pd

# Load cleaned data
df = pd.read_csv("mclaren_mcl38_cleaned.csv")

# Add product identification
df.insert(0, "Season", 2024)
df.insert(1, "Team", "McLaren")
df.insert(2, "Car", "MCL38")

# Save structured dataset
df.to_csv("mclaren_mcl38_structured.csv", index=False)

print("Data structured successfully!")
print("Rows:", len(df))
print("Columns:", len(df.columns))

print("\nColumns:")
print(df.columns.tolist())

print("\nFirst 5 rows:")
print(df.head().to_string(index=False))