import pandas as pd
import matplotlib.pyplot as plt


print("================================")
print("FINAL F1 PROJECT ANALYSIS")
print("================================")


# =========================================================
# 1. LOAD DATA
# =========================================================

final_df = pd.read_csv(
    "f1_final_mclaren_analysis.csv"
)

technical_df = pd.read_csv(
    "f1_technical_changes.csv"
)

performance_df = pd.read_csv(
    "f1_performance_change.csv"
)


print("\nFinal dataset loaded:", len(final_df), "rows")
print("Technical changes loaded:", len(technical_df), "rows")
print("Performance data loaded:", len(performance_df), "rows")


# =========================================================
# 2. DISPLAY FINAL COMPARISON
# =========================================================

print("\n================================")
print("McLAREN 2024 vs 2025")
print("================================")


comparison = final_df[
    [
        "Season",
        "Car",
        "Position",
        "Points",
        "Wins",
        "Weight",
        "Capacity",
        "Bank angle",
        "No of valves",
        "Max speed",
        "Max fuel flow rate",
        "Fuel injection",
        "Race wheels"
    ]
]


print(
    comparison.to_string(index=False)
)


# =========================================================
# 3. PERFORMANCE SUMMARY
# =========================================================

print("\n================================")
print("PERFORMANCE SUMMARY")
print("================================")


points_2024 = final_df.iloc[0]["Points"]
points_2025 = final_df.iloc[1]["Points"]

wins_2024 = final_df.iloc[0]["Wins"]
wins_2025 = final_df.iloc[1]["Wins"]


points_change = points_2025 - points_2024
wins_change = wins_2025 - wins_2024


points_percentage = (
    points_change / points_2024
) * 100


wins_percentage = (
    wins_change / wins_2024
) * 100


print(
    f"Points: {points_2024:.0f} → {points_2025:.0f}"
)

print(
    f"Points increase: +{points_change:.0f}"
)

print(
    f"Points percentage increase: "
    f"{points_percentage:.2f}%"
)


print(
    f"\nWins: {wins_2024:.0f} → {wins_2025:.0f}"
)

print(
    f"Wins increase: +{wins_change:.0f}"
)

print(
    f"Wins percentage increase: "
    f"{wins_percentage:.2f}%"
)


# =========================================================
# 4. TECHNICAL CHANGES
# =========================================================

print("\n================================")
print("TECHNICAL CHANGES")
print("================================")


if len(technical_df) > 0:

    print(
        technical_df.to_string(index=False)
    )

else:

    print(
        "No technical changes detected."
    )


# =========================================================
# 5. IDENTIFY UNCHANGED SPECIFICATIONS
# =========================================================

print("\n================================")
print("UNCHANGED SPECIFICATIONS")
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
    "Minimum weight"
]


unchanged = []


for column in technical_columns:

    if column not in final_df.columns:
        continue

    value_2024 = final_df.iloc[0][column]
    value_2025 = final_df.iloc[1][column]

    if pd.notna(value_2024) and pd.notna(value_2025):

        if value_2024 == value_2025:

            unchanged.append(
                column
            )


for item in unchanged:

    print(
        f"- {item}"
    )


print(
    "\nTotal unchanged specifications:",
    len(unchanged)
)


# =========================================================
# 6. CREATE FINAL PROJECT SUMMARY
# =========================================================

print("\n================================")
print("CREATING FINAL SUMMARY")
print("================================")


final_summary = pd.DataFrame(
    {
        "Category": [
            "Championship Points",
            "Race Wins",
            "Championship Position",
            "Car Weight",
            "Technical Changes",
            "Unchanged Technical Specifications"
        ],

        "2024": [
            points_2024,
            wins_2024,
            final_df.iloc[0]["Position"],
            final_df.iloc[0]["Weight"],
            "Baseline",
            len(unchanged)
        ],

        "2025": [
            points_2025,
            wins_2025,
            final_df.iloc[1]["Position"],
            final_df.iloc[1]["Weight"],
            len(technical_df),
            len(unchanged)
        ],

        "Change": [
            points_change,
            wins_change,
            final_df.iloc[1]["Position"]
            - final_df.iloc[0]["Position"],
            final_df.iloc[1]["Weight"]
            - final_df.iloc[0]["Weight"],
            len(technical_df),
            0
        ]
    }
)


print(
    final_summary.to_string(index=False)
)


# =========================================================
# 7. SAVE FINAL SUMMARY
# =========================================================

final_summary.to_csv(
    "f1_final_project_summary.csv",
    index=False
)


print(
    "\nFinal summary saved:"
)

print(
    "f1_final_project_summary.csv"
)


# =========================================================
# 8. GRAPH — POINTS AND WINS
# =========================================================

print("\n================================")
print("CREATING FINAL GRAPHS")
print("================================")


fig, ax1 = plt.subplots(
    figsize=(8, 5)
)


ax1.bar(
    final_df["Season"] - 0.15,
    final_df["Points"],
    width=0.3,
    label="Points"
)


ax1.set_xlabel(
    "Season"
)

ax1.set_ylabel(
    "Championship Points"
)


ax2 = ax1.twinx()


ax2.bar(
    final_df["Season"] + 0.15,
    final_df["Wins"],
    width=0.3,
    label="Wins"
)


ax2.set_ylabel(
    "Race Wins"
)


plt.title(
    "McLaren Performance Comparison: 2024 vs 2025"
)


fig.tight_layout()


plt.savefig(
    "14_final_performance_comparison.png",
    dpi=300
)


plt.close()


print(
    "Graph saved: "
    "14_final_performance_comparison.png"
)


# =========================================================
# 9. GRAPH — TECHNICAL CHANGES
# =========================================================

if len(technical_df) > 0:

    plt.figure(
        figsize=(10, 6)
    )

    plt.bar(
        technical_df["Specification"],
        technical_df["Change"]
    )

    plt.title(
        "McLaren Technical Changes: 2024 → 2025"
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
        "14_final_technical_changes.png",
        dpi=300
    )

    plt.close()

    print(
        "Graph saved: "
        "14_final_technical_changes.png"
    )


# =========================================================
# 10. FINAL PROJECT FINDINGS
# =========================================================

print("\n================================")
print("FINAL PROJECT FINDINGS")
print("================================")


print(
    "\n1. McLaren remained 1st in the "
    "constructors' championship."
)


print(
    f"2. Championship points increased "
    f"from {points_2024:.0f} to {points_2025:.0f}, "
    f"a {points_percentage:.2f}% increase."
)


print(
    f"3. Race wins increased "
    f"from {wins_2024:.0f} to {wins_2025:.0f}, "
    f"a {wins_percentage:.2f}% increase."
)


print(
    f"4. {len(technical_df)} numerical technical "
    "specification changes were detected."
)


print(
    f"5. {len(unchanged)} common numerical "
    "specifications remained unchanged."
)


print(
    "\n================================"
    "================"
)

print(
    "IMPORTANT INTERPRETATION"
)


print(
    "The results show that McLaren's performance "
    "improved substantially from 2024 to 2025 "
    "while only a limited number of extracted "
    "technical specifications changed."
)


print(
    "\nThis analysis shows an association between "
    "the observed technical data and performance."
)


print(
    "It does NOT establish that the identified "
    "technical changes directly caused the "
    "performance improvement."
)


print(
    "\nMore seasons, more teams, and more technical "
    "variables would be needed for stronger "
    "statistical conclusions."
)


# =========================================================
# 11. COMPLETION
# =========================================================

print("\n================================")
print("STEP 14 COMPLETED")
print("================================")


print(
    "\nFiles created:"
)

print(
    "f1_final_project_summary.csv"
)

print(
    "14_final_performance_comparison.png"
)

if len(technical_df) > 0:

    print(
        "14_final_technical_changes.png"
    )


print(
    "\nThe project has reached the final analysis stage."
)