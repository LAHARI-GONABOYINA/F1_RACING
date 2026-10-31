import pandas as pd
import matplotlib.pyplot as plt

print("================================")
print("STATISTICAL RELATIONSHIP ANALYSIS")
print("================================")

# =================================
# LOAD DATA
# =================================

technical_file = "18_quantitative_technical_changes.csv"
performance_file = "18_quantitative_performance.csv"

technical = pd.read_csv(technical_file)
performance = pd.read_csv(performance_file)

print("\nTechnical data loaded:", len(technical), "rows")
print("Performance data loaded:", len(performance), "rows")


# =================================
# PERFORMANCE CHANGES
# =================================

points_change = performance.loc[
    performance["Metric"] == "Championship Points",
    "Percentage Change"
].iloc[0]

wins_change = performance.loc[
    performance["Metric"] == "Race Wins",
    "Percentage Change"
].iloc[0]


print("\n================================")
print("PERFORMANCE CHANGE")
print("================================")

print(f"Championship points change: {points_change:.2f}%")
print(f"Race wins change: {wins_change:.2f}%")


# =================================
# TECHNICAL CHANGES
# =================================

changed = technical[
    technical["Status"] != "No change"
].copy()

print("\n================================")
print("CHANGED TECHNICAL FEATURES")
print("================================")

print(
    changed[
        [
            "Specification",
            "2024_Value",
            "2025_Value",
            "Absolute_Change",
            "Percentage_Change",
            "Status"
        ]
    ].to_string(index=False)
)


# =================================
# RELATIONSHIP TABLE
# =================================

relationship = []

for _, row in changed.iterrows():

    relationship.append({
        "Technical Specification": row["Specification"],
        "2024 Value": row["2024_Value"],
        "2025 Value": row["2025_Value"],
        "Technical Change": row["Absolute_Change"],
        "Technical % Change": row["Percentage_Change"],
        "Performance Points % Change": points_change,
        "Performance Wins % Change": wins_change
    })


relationship_df = pd.DataFrame(relationship)


print("\n================================")
print("TECHNICAL vs PERFORMANCE")
print("================================")

print(
    relationship_df.to_string(index=False)
)


# =================================
# SAVE RELATIONSHIP DATA
# =================================

relationship_df.to_csv(
    "19_technical_performance_relationship.csv",
    index=False
)

print(
    "\nRelationship analysis saved:"
    "\n19_technical_performance_relationship.csv"
)


# =================================
# CREATE PERFORMANCE CHANGE GRAPH
# =================================

metrics = [
    "Championship Points",
    "Race Wins"
]

changes = [
    points_change,
    wins_change
]

plt.figure(figsize=(8, 5))

plt.bar(metrics, changes)

plt.ylabel("Percentage Change (%)")

plt.title(
    "McLaren Performance Change: 2024 → 2025"
)

plt.axhline(0)

plt.tight_layout()

plt.savefig(
    "19_performance_percentage_change.png"
)

plt.close()

print(
    "Graph saved: 19_performance_percentage_change.png"
)


# =================================
# TECHNICAL CHANGE GRAPH
# =================================

numeric_changed = technical[
    technical["Status"].isin(
        ["Increased", "Decreased"]
    )
].copy()

if len(numeric_changed) > 0:

    plt.figure(figsize=(8, 5))

    plt.bar(
        numeric_changed["Specification"],
        numeric_changed["Percentage_Change"]
    )

    plt.ylabel("Technical Change (%)")

    plt.title(
        "McLaren Numerical Technical Changes"
    )

    plt.xticks(rotation=45)

    plt.axhline(0)

    plt.tight_layout()

    plt.savefig(
        "19_technical_percentage_change.png"
    )

    plt.close()

    print(
        "Graph saved: 19_technical_percentage_change.png"
    )


# =================================
# INTERPRETATION
# =================================

print("\n================================")
print("STATISTICAL INTERPRETATION")
print("================================")

print(
    "McLaren's championship points increased "
    f"by {points_change:.2f}%."
)

print(
    "McLaren's race wins increased "
    f"by {wins_change:.2f}%."
)

print(
    "\nThe extracted numerical technical data "
    "shows limited measurable changes."
)

print(
    "\nOnly Weight changed among the specifications "
    "available in both seasons."
)

print(
    "MGU-K and MGU-H appear as newly available "
    "2025 numerical specifications."
)

print(
    "\nIMPORTANT:"
)

print(
    "A statistical correlation cannot be reliably "
    "established from only two McLaren seasons."
)

print(
    "The results therefore describe observed "
    "changes rather than proving causation."
)


# =================================
# STEP COMPLETE
# =================================

print("\n================================")
print("STEP 19 COMPLETED")
print("================================")

print("\nFiles created:")
print("19_technical_performance_relationship.csv")
print("19_performance_percentage_change.png")
print("19_technical_percentage_change.png")