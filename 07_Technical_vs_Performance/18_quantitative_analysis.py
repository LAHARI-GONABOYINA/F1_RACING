import pandas as pd
import matplotlib.pyplot as plt

print("================================")
print("QUANTITATIVE TECHNICAL-PERFORMANCE ANALYSIS")
print("================================")

# =================================
# LOAD DATA
# =================================

file = "17_mclaren_technical_performance.csv"

df = pd.read_csv(file)

print("\nData loaded:")
print(df.to_string(index=False))


# =================================
# SORT BY SEASON
# =================================

df = df.sort_values("Season").reset_index(drop=True)

first = df.iloc[0]
second = df.iloc[1]


# =================================
# PERFORMANCE CHANGE
# =================================

points_change = second["Points"] - first["Points"]
wins_change = second["Wins"] - first["Wins"]

points_percent = (points_change / first["Points"]) * 100
wins_percent = (wins_change / first["Wins"]) * 100


print("\n================================")
print("PERFORMANCE CHANGE")
print("================================")

print(
    f"Points: {int(first['Points'])} → {int(second['Points'])}"
)

print(
    f"Points change: {points_change:+.0f}"
)

print(
    f"Points percentage change: {points_percent:+.2f}%"
)

print(
    f"\nWins: {int(first['Wins'])} → {int(second['Wins'])}"
)

print(
    f"Wins change: {wins_change:+.0f}"
)

print(
    f"Wins percentage change: {wins_percent:+.2f}%"
)


# =================================
# TECHNICAL CHANGES
# =================================

print("\n================================")
print("QUANTITATIVE TECHNICAL CHANGES")
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


technical_results = []

for column in technical_columns:

    if column not in df.columns:
        continue

    value_2024 = first[column]
    value_2025 = second[column]

    # Skip if either value is missing
    if pd.isna(value_2024) or pd.isna(value_2025):
        technical_results.append({
            "Specification": column,
            "2024_Value": value_2024,
            "2025_Value": value_2025,
            "Absolute_Change": None,
            "Percentage_Change": None,
            "Status": "New/Previously unavailable"
        })

        continue

    absolute_change = value_2025 - value_2024

    if value_2024 != 0:
        percentage_change = (
            absolute_change / value_2024
        ) * 100
    else:
        percentage_change = None

    if absolute_change > 0:
        status = "Increased"

    elif absolute_change < 0:
        status = "Decreased"

    else:
        status = "No change"

    technical_results.append({
        "Specification": column,
        "2024_Value": value_2024,
        "2025_Value": value_2025,
        "Absolute_Change": absolute_change,
        "Percentage_Change": percentage_change,
        "Status": status
    })


technical_df = pd.DataFrame(technical_results)

print(
    technical_df.to_string(index=False)
)


# =================================
# SAVE TECHNICAL ANALYSIS
# =================================

technical_df.to_csv(
    "18_quantitative_technical_changes.csv",
    index=False
)

print(
    "\nTechnical analysis saved:"
    "\n18_quantitative_technical_changes.csv"
)


# =================================
# PERFORMANCE SUMMARY
# =================================

performance_summary = pd.DataFrame({
    "Metric": [
        "Championship Points",
        "Race Wins"
    ],

    "2024": [
        first["Points"],
        first["Wins"]
    ],

    "2025": [
        second["Points"],
        second["Wins"]
    ],

    "Absolute Change": [
        points_change,
        wins_change
    ],

    "Percentage Change": [
        points_percent,
        wins_percent
    ]
})


print("\n================================")
print("PERFORMANCE SUMMARY")
print("================================")

print(
    performance_summary.to_string(index=False)
)


performance_summary.to_csv(
    "18_quantitative_performance.csv",
    index=False
)

print(
    "\nPerformance analysis saved:"
    "\n18_quantitative_performance.csv"
)


# =================================
# CREATE PERFORMANCE GRAPH
# =================================

plt.figure(figsize=(8, 5))

metrics = ["Points", "Wins"]

values_2024 = [
    first["Points"],
    first["Wins"]
]

values_2025 = [
    second["Points"],
    second["Wins"]
]

x = range(len(metrics))

width = 0.35

plt.bar(
    [i - width / 2 for i in x],
    values_2024,
    width=width,
    label="2024"
)

plt.bar(
    [i + width / 2 for i in x],
    values_2025,
    width=width,
    label="2025"
)

plt.xticks(x, metrics)

plt.ylabel("Value")

plt.title(
    "McLaren Quantitative Performance Change"
)

plt.legend()

plt.tight_layout()

plt.savefig(
    "18_quantitative_performance.png"
)

plt.close()

print(
    "Graph saved: 18_quantitative_performance.png"
)


# =================================
# FINAL INTERPRETATION
# =================================

print("\n================================")
print("ANALYSIS INTERPRETATION")
print("================================")

print(
    f"McLaren increased championship points "
    f"by {points_percent:.2f}%."
)

print(
    f"McLaren increased race wins "
    f"by {wins_percent:.2f}%."
)

print(
    "\nThe analysis also identifies which "
    "numerical technical specifications "
    "changed between 2024 and 2025."
)

print(
    "\nThese results show association only."
)

print(
    "They do NOT prove that a technical "
    "change directly caused the performance change."
)

print("\n================================")
print("STEP 18 COMPLETED")
print("================================")