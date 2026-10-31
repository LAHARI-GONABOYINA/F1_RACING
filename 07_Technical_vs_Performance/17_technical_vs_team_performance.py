import pandas as pd
import matplotlib.pyplot as plt

print("================================")
print("TECHNICAL vs TEAM PERFORMANCE")
print("================================")


# =================================
# LOAD DATA
# =================================

technical_file = "f1_specs_numeric_only.csv"
performance_file = "f1_multiteam_performance.csv"

technical = pd.read_csv(technical_file)
performance = pd.read_csv(performance_file)


print("\nTechnical data loaded:")
print("Rows:", len(technical))

print("\nPerformance data loaded:")
print(performance.to_string(index=False))


# =================================
# TECHNICAL DATA SUMMARY
# =================================

print("\n================================")
print("TECHNICAL SPECIFICATIONS")
print("================================")

print(
    technical[
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


# =================================
# TEAM PERFORMANCE
# =================================

print("\n================================")
print("TEAM PERFORMANCE")
print("================================")

print(performance.to_string(index=False))


# =================================
# MCLAREN TECHNICAL CHANGES
# =================================

print("\n================================")
print("MCLAREN TECHNICAL CHANGES")
print("================================")

mclaren = technical[
    technical["Team"].str.contains("McLaren", case=False, na=False)
].copy()

for specification in mclaren["Specification"].unique():

    data = mclaren[
        mclaren["Specification"] == specification
    ].sort_values("Season")

    if len(data) >= 2:

        first = data.iloc[0]
        second = data.iloc[-1]

        print(
            f"{specification}: "
            f"{first['Numeric_Value']} → "
            f"{second['Numeric_Value']}"
        )


# =================================
# PERFORMANCE COMPARISON
# =================================

print("\n================================")
print("PERFORMANCE COMPARISON")
print("================================")

for team in performance["Team"].unique():

    team_data = performance[
        performance["Team"] == team
    ].sort_values("Season")

    print(f"\n{team}")

    for _, row in team_data.iterrows():

        print(
            f"{int(row['Season'])}: "
            f"{int(row['Points'])} points, "
            f"{int(row['Wins'])} wins, "
            f"Position {int(row['Position'])}"
        )


# =================================
# MERGE TEAM + PERFORMANCE
# =================================

# Technical data is available for McLaren.
# Performance data contains McLaren and Mercedes.

mclaren_performance = performance[
    performance["Team"] == "McLaren"
].copy()


# =================================
# MCLAREN TECHNICAL-PERFORMANCE TABLE
# =================================

technical_features = technical[
    technical["Team"].str.contains(
        "McLaren",
        case=False,
        na=False
    )
].copy()


pivot = technical_features.pivot_table(
    index=["Season", "Team", "Car"],
    columns="Specification",
    values="Numeric_Value",
    aggfunc="first"
).reset_index()


mclaren_analysis = pd.merge(
    pivot,
    mclaren_performance,
    on=["Season", "Team"],
    how="inner"
)


print("\n================================")
print("MCLAREN TECHNICAL vs PERFORMANCE")
print("================================")

print(
    mclaren_analysis.to_string(index=False)
)


# =================================
# SAVE ANALYSIS DATA
# =================================

mclaren_analysis.to_csv(
    "17_mclaren_technical_performance.csv",
    index=False
)

print(
    "\nAnalysis file saved:"
    "\n17_mclaren_technical_performance.csv"
)


# =================================
# POINTS vs WEIGHT
# =================================

if "Weight" in mclaren_analysis.columns:

    plt.figure(figsize=(8, 5))

    plt.scatter(
        mclaren_analysis["Weight"],
        mclaren_analysis["Points"]
    )

    for _, row in mclaren_analysis.iterrows():

        plt.annotate(
            str(int(row["Season"])),
            (
                row["Weight"],
                row["Points"]
            )
        )

    plt.title(
        "McLaren Car Weight vs Championship Points"
    )

    plt.xlabel("Car Weight (kg)")
    plt.ylabel("Championship Points")

    plt.tight_layout()

    plt.savefig(
        "17_weight_vs_points.png"
    )

    plt.close()

    print(
        "Graph saved: 17_weight_vs_points.png"
    )


# =================================
# POINTS vs WINS
# =================================

plt.figure(figsize=(8, 5))

for team in performance["Team"].unique():

    team_data = performance[
        performance["Team"] == team
    ]

    plt.scatter(
        team_data["Wins"],
        team_data["Points"],
        label=team
    )

    for _, row in team_data.iterrows():

        plt.annotate(
            str(int(row["Season"])),
            (
                row["Wins"],
                row["Points"]
            )
        )


plt.title(
    "Race Wins vs Championship Points"
)

plt.xlabel("Race Wins")
plt.ylabel("Championship Points")

plt.legend()

plt.tight_layout()

plt.savefig(
    "17_wins_vs_points.png"
)

plt.close()

print(
    "Graph saved: 17_wins_vs_points.png"
)


# =================================
# FINAL INTERPRETATION
# =================================

print("\n================================")
print("STEP 17 COMPLETED")
print("================================")

print("""
This analysis connects the available
technical specifications with team
performance.

The analysis identifies relationships
between the available numerical
technical features and performance.

It does NOT prove that a particular
technical specification caused a
performance improvement.

More teams, seasons and technical
features are required for stronger
statistical analysis.
""")