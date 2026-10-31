import pandas as pd
import re


# =========================================================
# LOAD CLEANED TEXT DATA
# =========================================================

input_file = "f1_specs_cleaned_text.csv"

df = pd.read_csv(input_file)

print("================================")
print("FINAL NUMERICAL EXTRACTION")
print("================================")

print("\nInput file:", input_file)
print("Rows:", len(df))
print("Columns:", len(df.columns))


# =========================================================
# EXTRACT SPECIFIC NUMERICAL VALUES
# =========================================================

def extract_value(spec, value):

    if pd.isna(spec) or pd.isna(value):
        return None, None

    spec = str(spec).strip()
    value = str(value).strip()
    value_clean = value.replace(",", "")

    # -----------------------------------------------------
    # Weight
    # -----------------------------------------------------

    if spec == "Weight":
        match = re.search(r"(\d+(?:\.\d+)?)\s*kg", value_clean, re.I)

        if match:
            return float(match.group(1)), "kg"


    # -----------------------------------------------------
    # Minimum weight
    # -----------------------------------------------------

    if spec == "Minimum weight":
        match = re.search(r"(\d+(?:\.\d+)?)\s*kg", value_clean, re.I)

        if match:
            return float(match.group(1)), "kg"


    # -----------------------------------------------------
    # Weight distribution
    # -----------------------------------------------------

    if "Weight distribution" in spec:

        match = re.search(
            r"(\d+(?:\.\d+)?)\s*%\s*and\s*(\d+(?:\.\d+)?)\s*%",
            value_clean
        )

        if match:
            return (
                f"{match.group(1)} - {match.group(2)}",
                "%"
            )


    # -----------------------------------------------------
    # Race wheels
    # -----------------------------------------------------

    if spec == "Race wheels":

        match = re.search(
            r'(\d+(?:\.\d+)?)\s*[”"]',
            value
        )

        if match:
            return float(match.group(1)), "inch"


    # -----------------------------------------------------
    # Capacity
    # -----------------------------------------------------

    if spec == "Capacity":

        match = re.search(
            r"(\d+(?:\.\d+)?)\s*litres?",
            value_clean,
            re.I
        )

        if match:
            return float(match.group(1)), "litres"


    # -----------------------------------------------------
    # Bank angle
    # -----------------------------------------------------

    if spec == "Bank angle":

        match = re.search(
            r"(\d+(?:\.\d+)?)",
            value_clean
        )

        if match:
            return float(match.group(1)), "degree"


    # -----------------------------------------------------
    # Number of valves
    # -----------------------------------------------------

    if spec == "No of valves":

        match = re.search(
            r"(\d+(?:\.\d+)?)",
            value_clean
        )

        if match:
            return float(match.group(1)), "valves"


    # -----------------------------------------------------
    # Maximum speed
    # -----------------------------------------------------

    if spec == "Max speed":

        match = re.search(
            r"(\d+(?:\.\d+)?)\s*rpm",
            value_clean,
            re.I
        )

        if match:
            return float(match.group(1)), "rpm"


    # -----------------------------------------------------
    # Maximum fuel flow rate
    # -----------------------------------------------------

    if spec == "Max fuel flow rate":

        match = re.search(
            r"(\d+(?:\.\d+)?)\s*kg/hour",
            value_clean,
            re.I
        )

        if match:
            return float(match.group(1)), "kg/hour"


    # -----------------------------------------------------
    # Fuel injection
    # -----------------------------------------------------

    if spec == "Fuel injection":

        match = re.search(
            r"(\d+(?:\.\d+)?)\s*bar",
            value_clean,
            re.I
        )

        if match:
            return float(match.group(1)), "bar"


    # -----------------------------------------------------
    # MGU-K
    # -----------------------------------------------------

    if spec == "MGU-K":

        match = re.search(
            r"Maximum speed\s*(\d+(?:\.\d+)?)\s*rpm",
            value_clean,
            re.I
        )

        if match:
            return float(match.group(1)), "rpm"


    # -----------------------------------------------------
    # MGU-H
    # -----------------------------------------------------

    if spec == "MGU-H":

        match = re.search(
            r"Maximum speed\s*(\d+(?:\.\d+)?)\s*rpm",
            value_clean,
            re.I
        )

        if match:
            return float(match.group(1)), "rpm"


    # -----------------------------------------------------
    # No valid numerical value
    # -----------------------------------------------------

    return None, None


# =========================================================
# APPLY EXTRACTION
# =========================================================

results = df.apply(
    lambda row: extract_value(
        row["Specification"],
        row["Value"]
    ),
    axis=1
)


# =========================================================
# CREATE NEW COLUMNS
# =========================================================

df["Numeric_Value"] = [
    result[0]
    for result in results
]

df["Unit"] = [
    result[1]
    for result in results
]


# =========================================================
# NUMERICAL DATASET
# =========================================================

numeric_df = df[
    df["Numeric_Value"].notna()
].copy()


# =========================================================
# DISPLAY RESULTS
# =========================================================

print("\n================================")
print("VALID NUMERICAL SPECIFICATIONS")
print("================================")

print(
    numeric_df[
        [
            "Season",
            "Team",
            "Car",
            "Specification",
            "Numeric_Value",
            "Unit"
        ]
    ].to_string(index=False)
)


# =========================================================
# SUMMARY
# =========================================================

print("\n================================")
print("EXTRACTION SUMMARY")
print("================================")

print("Original rows:", len(df))

print(
    "Numerical rows:",
    len(numeric_df)
)

print(
    "Non-numerical rows:",
    len(df) - len(numeric_df)
)


# =========================================================
# SHOW NUMERICAL DATA PER CAR
# =========================================================

print("\n================================")
print("ROWS PER CAR")
print("================================")

rows_per_car = (
    numeric_df
    .groupby(["Season", "Team", "Car"])
    .size()
    .reset_index(name="Rows")
)

print(
    rows_per_car.to_string(index=False)
)


# =========================================================
# SAVE COMPLETE DATASET
# =========================================================

df.to_csv(
    "f1_specs_numeric.csv",
    index=False
)


# =========================================================
# SAVE NUMERICAL-ONLY DATASET
# =========================================================

numeric_df.to_csv(
    "f1_specs_numeric_only.csv",
    index=False
)


# =========================================================
# FINAL MESSAGE
# =========================================================

print("\n================================")
print("FINAL EXTRACTION COMPLETED")
print("================================")

print("\nComplete dataset saved:")
print("f1_specs_numeric.csv")

print("\nNumerical-only dataset saved:")
print("f1_specs_numeric_only.csv")