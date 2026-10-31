import pandas as pd
import matplotlib.pyplot as plt


# =========================================================
# LOAD NUMERICAL DATA
# =========================================================

file = "f1_specs_numeric_only.csv"

df = pd.read_csv(file)

print("================================")
print("TECHNICAL SPECIFICATION ANALYSIS")
print("================================")

print("\nInput file:", file)
print("Rows:", len(df))
print("Columns:", len(df.columns))


# =========================================================
# KEEP ONLY MCLAREN CARS
# =========================================================

mclaren = df[df["Team"] == "McLaren"].copy()

print("\nMcLaren cars available:")

print(
    mclaren[["Season", "Team", "Car"]]
    .drop_duplicates()
    .to_string(index=False)
)


# =========================================================
# SPECIFICATIONS WE WANT TO COMPARE
# =========================================================

specifications = [
    "Weight",
    "Minimum weight",
    "Capacity",
    "Bank angle",
    "No of valves",
    "Max speed",
    "Max fuel flow rate",
    "Fuel injection",
    "Race wheels"
]


# =========================================================
# CREATE COMPARISON DATA
# =========================================================

comparison = []

for spec in specifications:

    temp = mclaren[
        mclaren["Specification"].str.strip().str.lower()
        == spec.lower()
    ].copy()

    if len(temp) == 0:
        continue

    for _, row in temp.iterrows():

        comparison.append([
            row["Season"],
            row["Car"],
            row["Specification"],
            row["Numeric_Value"],
            row["Unit"]
        ])


comparison_df = pd.DataFrame(
    comparison,
    columns=[
        "Season",
        "Car",
        "Specification",
        "Numeric_Value",
        "Unit"
    ]
)


# =========================================================
# DISPLAY COMPARISON DATA
# =========================================================

print("\n================================")
print("COMMON TECHNICAL SPECIFICATIONS")
print("================================")

print(
    comparison_df.to_string(index=False)
)


# =========================================================
# SAVE COMPARISON DATA
# =========================================================

comparison_df.to_csv(
    "mclaren_technical_comparison.csv",
    index=False
)

print(
    "\nComparison data saved:"
    " mclaren_technical_comparison.csv"
)


# =========================================================
# CREATE GRAPHS
# =========================================================

print("\n================================")
print("CREATING COMPARISON GRAPHS")
print("================================")


for spec in comparison_df["Specification"].unique():

    temp = comparison_df[
        comparison_df["Specification"] == spec
    ].copy()

    # Need at least 2 cars for comparison
    if temp["Car"].nunique() < 2:
        continue

    plt.figure(figsize=(8, 5))

    plt.bar(
        temp["Car"],
        temp["Numeric_Value"]
    )

    unit = temp["Unit"].iloc[0]

    plt.title(
        "McLaren F1 Car Comparison - " + spec
    )

    plt.xlabel("F1 Car")

    if pd.notna(unit):
        plt.ylabel(
            spec + " (" + str(unit) + ")"
        )
    else:
        plt.ylabel(spec)

    plt.tight_layout()

    # Create safe filename
    filename = (
        "mclaren_"
        + spec.lower()
        .replace(" ", "_")
        .replace("/", "_")
        + ".png"
    )

    plt.savefig(
        filename,
        dpi=300
    )

    print(
        "Graph saved:",
        filename
    )

    plt.show()


# =========================================================
# FINAL MESSAGE
# =========================================================

print("\n================================")
print("ANALYSIS COMPLETED")
print("================================")

print(
    "\nComparison file:"
    " mclaren_technical_comparison.csv"
)

print(
    "\nTechnical comparison graphs created successfully."
)