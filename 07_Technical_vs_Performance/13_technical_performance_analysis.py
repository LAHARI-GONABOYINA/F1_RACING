import pandas as pd
import matplotlib.pyplot as plt


print("================================")
print("TECHNICAL vs PERFORMANCE ANALYSIS")
print("================================")


# =========================================================
# 1. LOAD FINAL DATASET
# =========================================================

file = "f1_final_mclaren_analysis.csv"

df = pd.read_csv(file)

print("\nInput file:", file)
print("Rows:", len(df))
print("Columns:", len(df.columns))


# =========================================================
# 2. DISPLAY BASIC DATA
# =========================================================

print("\n================================")
print("McLAREN PERFORMANCE")
print("================================")

print(
    df[
        ["Season", "Car", "Position", "Points", "Wins"]
    ].to_string(index=False)
)


# =========================================================
# 3. GET 2024 AND 2025 DATA
# =========================================================

year_2024 = df[df["Season"] == 2024].iloc[0]
year_2025 = df[df["Season"] == 2025].iloc[0]


# =========================================================
# 4. PERFORMANCE CHANGE
# =========================================================

points_2024 = year_2024["Points"]
points_2025 = year_2025["Points"]

wins_2024 = year_2024["Wins"]
wins_2025 = year_2025["Wins"]


points_change = points_2025 - points_2024
wins_change = wins_2025 - wins_2024


points_percentage = (
    points_change / points_2024
) * 100


wins_percentage = (
    wins_change / wins_2024
) * 100


print("\n================================")
print("PERFORMANCE CHANGE")
print("================================")

print(
    f"\nPoints: {points_2024:.0f} → "
    f"{points_2025:.0f}"
)

print(
    f"Points change: +{points_change:.0f}"
)

print(
    f"Points improvement: "
    f"{points_percentage:.2f}%"
)


print(
    f"\nWins: {wins_2024:.0f} → "
    f"{wins_2025:.0f}"
)

print(
    f"Wins change: +{wins_change:.0f}"
)

print(
    f"Wins improvement: "
    f"{wins_percentage:.2f}%"
)


# =========================================================
# 5. IDENTIFY TECHNICAL CHANGES
# =========================================================

print("\n================================")
print("TECHNICAL SPECIFICATION CHANGES")
print("================================")


technical_columns = [
    "Weight",
    "Capacity",
    "Bank angle",
    "No of valves",
    "Max speed",
    "Max fuel flow rate",
    "Fuel injection",
    "Race wheels",
    "Minimum weight",
    "MGU-K",
    "MGU-H"
]


technical_changes = []


for column in technical_columns:

    if column not in df.columns:
        continue

    value_2024 = year_2024[column]
    value_2025 = year_2025[column]

    # Both values must exist
    if pd.notna(value_2024) and pd.notna(value_2025):

        change = value_2025 - value_2024

        if change != 0:

            technical_changes.append(
                {
                    "Specification": column,
                    "2024_Value": value_2024,
                    "2025_Value": value_2025,
                    "Change": change
                }
            )

            print(
                f"{column}: "
                f"{value_2024} → {value_2025} "
                f"(Change: {change:+.2f})"
            )

    # New specification appearing in 2025
    elif pd.isna(value_2024) and pd.notna(value_2025):

        technical_changes.append(
            {
                "Specification": column,
                "2024_Value": value_2024,
                "2025_Value": value_2025,
                "Change": value_2025
            }
        )

        print(
            f"{column}: "
            f"Not available in 2024 → "
            f"{value_2025} in 2025"
        )


# =========================================================
# 6. CREATE TECHNICAL CHANGE DATAFRAME
# =========================================================

technical_change_df = pd.DataFrame(
    technical_changes
)


print("\n================================")
print("CHANGED TECHNICAL FEATURES")
print("================================")


if len(technical_change_df) > 0:

    print(
        technical_change_df.to_string(
            index=False
        )
    )

else:

    print(
        "No numerical technical specifications changed."
    )


# =========================================================
# 7. SAVE TECHNICAL CHANGES
# =========================================================

technical_change_df.to_csv(
    "f1_technical_changes.csv",
    index=False
)

print(
    "\nTechnical changes saved:"
)

print(
    "f1_technical_changes.csv"
)


# =========================================================
# 8. CREATE PERFORMANCE SUMMARY
# =========================================================

summary = pd.DataFrame(
    {
        "Metric": [
            "Championship Points",
            "Race Wins"
        ],

        "2024": [
            points_2024,
            wins_2024
        ],

        "2025": [
            points_2025,
            wins_2025
        ],

        "Change": [
            points_change,
            wins_change
        ],

        "Percentage Change": [
            points_percentage,
            wins_percentage
        ]
    }
)


print("\n================================")
print("PERFORMANCE SUMMARY")
print("================================")

print(
    summary.to_string(index=False)
)


# =========================================================
# 9. SAVE PERFORMANCE SUMMARY
# =========================================================

summary.to_csv(
    "f1_performance_change.csv",
    index=False
)

print(
    "\nPerformance summary saved:"
)

print(
    "f1_performance_change.csv"
)


# =========================================================
# 10. GRAPH — POINTS VS WINS
# =========================================================

print("\n================================")
print("CREATING PERFORMANCE GRAPH")
print("================================")


fig, ax1 = plt.subplots(
    figsize=(8, 5)
)


# Points
ax1.plot(
    df["Season"],
    df["Points"],
    marker="o",
    linewidth=2,
    label="Championship Points"
)

ax1.set_xlabel("Season")

ax1.set_ylabel(
    "Championship Points"
)


# Wins on second axis
ax2 = ax1.twinx()

ax2.plot(
    df["Season"],
    df["Wins"],
    marker="s",
    linewidth=2,
    label="Race Wins"
)

ax2.set_ylabel(
    "Race Wins"
)


plt.title(
    "McLaren Performance: 2024 vs 2025"
)

fig.tight_layout()

plt.savefig(
    "13_mclaren_performance_change.png",
    dpi=300
)

plt.close()


print(
    "Graph saved: "
    "13_mclaren_performance_change.png"
)


# =========================================================
# 11. TECHNICAL CHANGE GRAPH
# =========================================================

if len(technical_change_df) > 0:

    print(
        "\nCreating technical change graph..."
    )

    plt.figure(
        figsize=(10, 6)
    )

    plt.bar(
        technical_change_df["Specification"],
        technical_change_df["Change"]
    )

    plt.title(
        "McLaren Technical Specification Changes"
    )

    plt.xlabel(
        "Technical Specification"
    )

    plt.ylabel(
        "Change"
    )

    plt.xticks(
        rotation=45,
        ha="right"
    )

    plt.tight_layout()

    plt.savefig(
        "13_mclaren_technical_changes.png",
        dpi=300
    )

    plt.close()

    print(
        "Graph saved: "
        "13_mclaren_technical_changes.png"
    )


# =========================================================
# 12. INTERPRETATION
# =========================================================

print("\n================================")
print("ANALYSIS INTERPRETATION")
print("================================")


print(
    "\nMcLaren's championship points increased "
    f"by {points_percentage:.2f}% from 2024 to 2025."
)


print(
    "McLaren's race wins increased "
    f"by {wins_percentage:.2f}% from 2024 to 2025."
)


if len(technical_change_df) > 0:

    print(
        "\nThe numerical technical specifications "
        "showing changes were:"
    )

    for _, row in technical_change_df.iterrows():

        print(
            f"- {row['Specification']}"
        )

else:

    print(
        "\nNo numerical technical specification "
        "changes were detected."
    )


print(
    "\nImportant:"
)

print(
    "The analysis identifies changes occurring "
    "between the two seasons."
)

print(
    "It does NOT prove that a specific technical "
    "change caused the performance improvement."
)

print(
    "More seasons or more teams would be required "
    "to establish a stronger relationship."
)


# =========================================================
# 13. FINAL MESSAGE
# =========================================================

print("\n================================")
print("STEP 13 COMPLETED")
print("================================")

print(
    "\nFiles created:"
)

print(
    "f1_technical_changes.csv"
)

print(
    "f1_performance_change.csv"
)

print(
    "13_mclaren_performance_change.png"
)

if len(technical_change_df) > 0:

    print(
        "13_mclaren_technical_changes.png"
    )

print(
    "\nReady for the next analysis stage."
)