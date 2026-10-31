import pandas as pd

print("================================")
print("CREATING MULTI-TEAM PERFORMANCE DATA")
print("================================")

# Load scraped team performance
df = pd.read_csv("f1_performance_raw.csv")

print("\nPerformance data loaded:")
print(df.to_string(index=False))


# Normalize team names
def normalize_team(team):

    team = str(team)

    if "McLaren" in team:
        return "McLaren"

    if "Mercedes" in team:
        return "Mercedes"

    if "Ferrari" in team:
        return "Ferrari"

    if "Red Bull" in team:
        return "Red Bull Racing"

    return team


df["Team"] = df["Team"].apply(normalize_team)


# Keep the four teams
required_teams = [
    "McLaren",
    "Mercedes",
    "Ferrari",
    "Red Bull Racing"
]

df = df[df["Team"].isin(required_teams)].copy()

df = df[
    [
        "Season",
        "Position",
        "Team",
        "Points"
    ]
]


# Load wins
wins = pd.read_csv("f1_team_wins.csv")

wins["Team"] = wins["Team"].apply(normalize_team)

wins = wins[wins["Team"].isin(required_teams)]

wins = wins[
    [
        "Season",
        "Team",
        "Wins"
    ]
]


# Merge performance and wins
final = pd.merge(
    df,
    wins,
    on=["Season", "Team"],
    how="left"
)

final["Wins"] = final["Wins"].fillna(0)

final = final.sort_values(
    ["Season", "Position"]
)


print("\n================================")
print("FINAL MULTI-TEAM PERFORMANCE DATA")
print("================================")

print(final.to_string(index=False))


# Save
final.to_csv(
    "f1_multiteam_performance.csv",
    index=False
)


print("\n================================")
print("STEP 15 COMPLETED")
print("================================")

print("\nFile created:")
print("f1_multiteam_performance.csv")

print("\nRows created:", len(final))