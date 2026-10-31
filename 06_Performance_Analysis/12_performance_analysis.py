import pandas as pd
import matplotlib.pyplot as plt


print("================================")
print("F1 PERFORMANCE ANALYSIS")
print("================================")


# =========================================================
# 1. LOAD FINAL DATASET
# =========================================================

df = pd.read_csv("f1_final_mclaren_analysis.csv")

print("\nInput file: f1_final_mclaren_analysis.csv")
print("Rows:", len(df))
print("Columns:", len(df.columns))


# =========================================================
# 2. DISPLAY PERFORMANCE DATA
# =========================================================

print("\n================================")
print("PERFORMANCE DATA")
print("================================")

performance = df[
    ["Season", "Team", "Car", "Position", "Points", "Wins"]
]

print(
    performance.to_string(index=False)
)


# =========================================================
# 3. POINTS COMPARISON
# =========================================================

print("\n================================")
print("POINTS COMPARISON")
print("================================")

for _, row in df.iterrows():

    print(
        f"{int(row['Season'])} {row['Car']}: "
        f"{int(row['Points'])} points"
    )


points_change = (
    df.iloc[1]["Points"] -
    df.iloc[0]["Points"]
)

points_percentage = (
    points_change /
    df.iloc[0]["Points"]
) * 100


print(
    f"\nPoints increased by {points_change:.0f}"
)

print(
    f"Percentage increase: "
    f"{points_percentage:.2f}%"
)


# =========================================================
# 4. WINS COMPARISON
# =========================================================

print("\n================================")
print("WINS COMPARISON")
print("================================")

for _, row in df.iterrows():

    print(
        f"{int(row['Season'])} {row['Car']}: "
        f"{int(row['Wins'])} wins"
    )


wins_change = (
    df.iloc[1]["Wins"] -
    df.iloc[0]["Wins"]
)

wins_percentage = (
    wins_change /
    df.iloc[0]["Wins"]
) * 100


print(
    f"\nWins increased by {wins_change:.0f}"
)

print(
    f"Percentage increase: "
    f"{wins_percentage:.2f}%"
)


# =========================================================
# 5. CHAMPIONSHIP POSITION
# =========================================================

print("\n================================")
print("CHAMPIONSHIP POSITION")
print("================================")

for _, row in df.iterrows():

    print(
        f"{int(row['Season'])} {row['Car']}: "
        f"{int(row['Position'])} position"
    )


# =========================================================
# 6. TECHNICAL CHANGES
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
    "Minimum weight"
]


for column in technical_columns:

    if column in df.columns:

        old_value = df.iloc[0][column]
        new_value = df.iloc[1][column]

        if pd.notna(old_value) and pd.notna(new_value):

            change = new_value - old_value

            print(
                f"{column}: "
                f"{old_value} → {new_value} "
                f"(Change: {change:+.2f})"
            )


# =========================================================
# 7. GRAPH 1 — POINTS
# =========================================================

print("\n================================")
print("CREATING PERFORMANCE GRAPHS")
print("================================")


plt.figure(figsize=(8, 5))

plt.bar(
    df["Car"],
    df["Points"]
)

plt.title(
    "McLaren Championship Points: 2024 vs 2025"
)

plt.xlabel("Car")

plt.ylabel("Championship Points")

plt.tight_layout()

plt.savefig(
    "12_mclaren_points_comparison.png",
    dpi=300
)

plt.close()

print(
    "Graph saved: "
    "12_mclaren_points_comparison.png"
)


# =========================================================
# 8. GRAPH 2 — WINS
# =========================================================

plt.figure(figsize=(8, 5))

plt.bar(
    df["Car"],
    df["Wins"]
)

plt.title(
    "McLaren Race Wins: 2024 vs 2025"
)

plt.xlabel("Car")

plt.ylabel("Number of Wins")

plt.tight_layout()

plt.savefig(
    "12_mclaren_wins_comparison.png",
    dpi=300
)

plt.close()

print(
    "Graph saved: "
    "12_mclaren_wins_comparison.png"
)


# =========================================================
# 9. GRAPH 3 — WEIGHT
# =========================================================

plt.figure(figsize=(8, 5))

plt.bar(
    df["Car"],
    df["Weight"]
)

plt.title(
    "McLaren Car Weight: 2024 vs 2025"
)

plt.xlabel("Car")

plt.ylabel("Weight (kg)")

plt.tight_layout()

plt.savefig(
    "12_mclaren_weight_comparison.png",
    dpi=300
)

plt.close()

print(
    "Graph saved: "
    "12_mclaren_weight_comparison.png"
)


# =========================================================
# 10. FINAL SUMMARY
# =========================================================

print("\n================================")
print("PERFORMANCE ANALYSIS COMPLETED")
print("================================")

print(
    f"\nMcLaren points: "
    f"{df.iloc[0]['Points']:.0f} → "
    f"{df.iloc[1]['Points']:.0f}"
)

print(
    f"McLaren wins: "
    f"{df.iloc[0]['Wins']:.0f} → "
    f"{df.iloc[1]['Wins']:.0f}"
)

print(
    f"Car weight: "
    f"{df.iloc[0]['Weight']:.0f} kg → "
    f"{df.iloc[1]['Weight']:.0f} kg"
)

print(
    "\nFiles created:"
)

print(
    "12_mclaren_points_comparison.png"
)

print(
    "12_mclaren_wins_comparison.png"
)

print(
    "12_mclaren_weight_comparison.png"
)