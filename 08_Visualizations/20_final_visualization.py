import pandas as pd
import matplotlib.pyplot as plt

print("================================")
print("FINAL F1 VISUALIZATION")
print("================================")

# =================================
# LOAD DATA
# =================================

performance = pd.read_csv(
    "f1_multiteam_performance.csv"
)

technical = pd.read_csv(
    "18_quantitative_technical_changes.csv"
)

print("\nPerformance data loaded:")
print(performance.to_string(index=False))


# =================================
# 1. TEAM POINTS COMPARISON
# =================================

print("\n================================")
print("CREATING TEAM POINTS GRAPH")
print("================================")

teams = performance["Team"].unique()
seasons = sorted(performance["Season"].unique())

plt.figure(figsize=(9, 5))

for team in teams:

    team_data = performance[
        performance["Team"] == team
    ]

    points = []

    for season in seasons:

        row = team_data[
            team_data["Season"] == season
        ]

        if len(row) > 0:
            points.append(
                row["Points"].iloc[0]
            )
        else:
            points.append(None)

    plt.plot(
        seasons,
        points,
        marker="o",
        linewidth=2,
        label=team
    )

plt.xlabel("Season")
plt.ylabel("Championship Points")
plt.title(
    "F1 Team Championship Points: 2024 vs 2025"
)

plt.legend()
plt.grid(True)

plt.tight_layout()

plt.savefig(
    "20_team_points_trend.png"
)

plt.close()

print(
    "Graph saved: 20_team_points_trend.png"
)


# =================================
# 2. TEAM WINS COMPARISON
# =================================

print("\n================================")
print("CREATING TEAM WINS GRAPH")
print("================================")

plt.figure(figsize=(9, 5))

for team in teams:

    team_data = performance[
        performance["Team"] == team
    ]

    wins = []

    for season in seasons:

        row = team_data[
            team_data["Season"] == season
        ]

        if len(row) > 0:
            wins.append(
                row["Wins"].iloc[0]
            )
        else:
            wins.append(None)

    plt.plot(
        seasons,
        wins,
        marker="o",
        linewidth=2,
        label=team
    )

plt.xlabel("Season")
plt.ylabel("Race Wins")

plt.title(
    "F1 Team Race Wins: 2024 vs 2025"
)

plt.legend()
plt.grid(True)

plt.tight_layout()

plt.savefig(
    "20_team_wins_trend.png"
)

plt.close()

print(
    "Graph saved: 20_team_wins_trend.png"
)


# =================================
# 3. MCLAREN PERFORMANCE CHANGE
# =================================

print("\n================================")
print("CREATING MCLAREN PERFORMANCE GRAPH")
print("================================")

mclaren = performance[
    performance["Team"] == "McLaren"
].sort_values("Season")

plt.figure(figsize=(8, 5))

plt.bar(
    mclaren["Season"].astype(str),
    mclaren["Points"]
)

plt.xlabel("Season")
plt.ylabel("Championship Points")

plt.title(
    "McLaren Championship Points Improvement"
)

plt.tight_layout()

plt.savefig(
    "20_mclaren_points_final.png"
)

plt.close()

print(
    "Graph saved: 20_mclaren_points_final.png"
)


# =================================
# 4. TECHNICAL CHANGES
# =================================

print("\n================================")
print("CREATING TECHNICAL CHANGE GRAPH")
print("================================")

changed = technical[
    technical["Status"] != "No change"
].copy()

# Only numerical percentage changes
plot_data = changed[
    changed["Percentage_Change"].notna()
]

if len(plot_data) > 0:

    plt.figure(figsize=(9, 5))

    plt.bar(
        plot_data["Specification"],
        plot_data["Percentage_Change"]
    )

    plt.xlabel("Technical Specification")
    plt.ylabel("Percentage Change (%)")

    plt.title(
        "McLaren Numerical Technical Changes"
    )

    plt.xticks(rotation=45)

    plt.tight_layout()

    plt.savefig(
        "20_mclaren_technical_changes_final.png"
    )

    plt.close()

    print(
        "Graph saved: "
        "20_mclaren_technical_changes_final.png"
    )


# =================================
# 5. CREATE DASHBOARD DATA
# =================================

print("\n================================")
print("CREATING DASHBOARD DATA")
print("================================")

dashboard = pd.DataFrame({
    "Metric": [
        "McLaren 2024 Points",
        "McLaren 2025 Points",
        "McLaren Points Increase %",
        "McLaren 2024 Wins",
        "McLaren 2025 Wins",
        "McLaren Wins Increase %",
        "McLaren 2024 Position",
        "McLaren 2025 Position"
    ],

    "Value": [
        666,
        833,
        25.08,
        6,
        14,
        133.33,
        1,
        1
    ]
})

print(
    dashboard.to_string(index=False)
)

dashboard.to_csv(
    "20_final_dashboard_data.csv",
    index=False
)

print(
    "\nDashboard data saved:"
    "\n20_final_dashboard_data.csv"
)


# =================================
# FINAL SUMMARY
# =================================

print("\n================================")
print("STEP 20 COMPLETED")
print("================================")

print("\nFinal visualization files:")

print("20_team_points_trend.png")
print("20_team_wins_trend.png")
print("20_mclaren_points_final.png")
print("20_mclaren_technical_changes_final.png")
print("20_final_dashboard_data.csv")

print("\nThese outputs are ready for")
print("the final project presentation.")