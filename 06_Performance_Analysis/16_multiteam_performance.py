import pandas as pd
import matplotlib.pyplot as plt

print("================================")
print("MULTI-TEAM PERFORMANCE ANALYSIS")
print("================================")

# Load data
df = pd.read_csv("f1_multiteam_performance.csv")

print("\nData loaded:")
print(df.to_string(index=False))


# --------------------------------
# PERFORMANCE COMPARISON
# --------------------------------

print("\n================================")
print("TEAM PERFORMANCE COMPARISON")
print("================================")

for team in df["Team"].unique():

    team_data = df[df["Team"] == team]

    print(f"\n{team}")

    for _, row in team_data.iterrows():

        print(
            f"{int(row['Season'])}: "
            f"{int(row['Points'])} points, "
            f"{int(row['Wins'])} wins, "
            f"Position {int(row['Position'])}"
        )


# --------------------------------
# CREATE POINTS GRAPH
# --------------------------------

print("\n================================")
print("CREATING GRAPHS")
print("================================")

pivot_points = df.pivot(
    index="Season",
    columns="Team",
    values="Points"
)

pivot_points.plot(
    kind="bar",
    figsize=(8, 5)
)

plt.title("F1 Team Championship Points Comparison")
plt.xlabel("Season")
plt.ylabel("Championship Points")
plt.xticks(rotation=0)
plt.tight_layout()

plt.savefig("16_team_points_comparison.png")
plt.close()

print("Graph saved: 16_team_points_comparison.png")


# --------------------------------
# CREATE WINS GRAPH
# --------------------------------

pivot_wins = df.pivot(
    index="Season",
    columns="Team",
    values="Wins"
)

pivot_wins.plot(
    kind="bar",
    figsize=(8, 5)
)

plt.title("F1 Team Race Wins Comparison")
plt.xlabel("Season")
plt.ylabel("Race Wins")
plt.xticks(rotation=0)
plt.tight_layout()

plt.savefig("16_team_wins_comparison.png")
plt.close()

print("Graph saved: 16_team_wins_comparison.png")


# --------------------------------
# PERFORMANCE CHANGE
# --------------------------------

print("\n================================")
print("2024 → 2025 PERFORMANCE CHANGE")
print("================================")

changes = []

for team in df["Team"].unique():

    team_data = df[df["Team"] == team].sort_values("Season")

    if len(team_data) == 2:

        first = team_data.iloc[0]
        second = team_data.iloc[1]

        points_change = second["Points"] - first["Points"]
        wins_change = second["Wins"] - first["Wins"]

        changes.append({
            "Team": team,
            "Points_2024": first["Points"],
            "Points_2025": second["Points"],
            "Points_Change": points_change,
            "Wins_2024": first["Wins"],
            "Wins_2025": second["Wins"],
            "Wins_Change": wins_change
        })

        print(f"\n{team}")
        print(f"Points: {int(first['Points'])} → {int(second['Points'])}")
        print(f"Points change: {int(points_change):+d}")
        print(f"Wins: {int(first['Wins'])} → {int(second['Wins'])}")
        print(f"Wins change: {int(wins_change):+d}")


# --------------------------------
# SAVE CHANGE DATA
# --------------------------------

change_df = pd.DataFrame(changes)

change_df.to_csv(
    "16_team_performance_change.csv",
    index=False
)

print("\nPerformance change file saved:")
print("16_team_performance_change.csv")


print("\n================================")
print("STEP 16 COMPLETED")
print("================================")