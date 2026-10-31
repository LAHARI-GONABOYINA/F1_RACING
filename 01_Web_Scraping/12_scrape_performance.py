import requests
from bs4 import BeautifulSoup
import pandas as pd


# =========================================================
# SCRAPE F1 TEAM STANDINGS
# =========================================================

def scrape_team_standings(season):

    print(f"\nScraping {season} F1 Team Standings...")

    url = f"https://www.formula1.com/en/results/{season}/team"

    response = requests.get(
        url,
        headers={
            "User-Agent": "Mozilla/5.0"
        },
        timeout=20
    )

    print("Status code:", response.status_code)

    if response.status_code != 200:
        print("Could not access the page.")
        return None

    soup = BeautifulSoup(response.text, "html.parser")

    table = soup.find("table")

    if table is None:
        print("No standings table found.")
        return None

    rows = table.find_all("tr")

    data = []

    for row in rows:

        cells = row.find_all(["th", "td"])

        values = [
            cell.get_text(" ", strip=True)
            for cell in cells
        ]

        # Skip header
        if values == ["Pos.", "Team", "Pts."]:
            continue

        if len(values) == 3:

            position = values[0]
            team = values[1]
            points = values[2]

            data.append([
                season,
                position,
                team,
                points
            ])

    df = pd.DataFrame(
        data,
        columns=[
            "Season",
            "Position",
            "Team",
            "Points"
        ]
    )

    print("Rows scraped:", len(df))

    return df


# =========================================================
# SCRAPE 2024
# =========================================================

df_2024 = scrape_team_standings(2024)


# =========================================================
# SCRAPE 2025
# =========================================================

df_2025 = scrape_team_standings(2025)


# =========================================================
# COMBINE DATA
# =========================================================

dataframes = []

if df_2024 is not None:
    dataframes.append(df_2024)

if df_2025 is not None:
    dataframes.append(df_2025)


if dataframes:

    final_df = pd.concat(
        dataframes,
        ignore_index=True
    )

    # Convert numerical columns
    final_df["Season"] = pd.to_numeric(
        final_df["Season"]
    )

    final_df["Position"] = pd.to_numeric(
        final_df["Position"]
    )

    final_df["Points"] = pd.to_numeric(
        final_df["Points"]
    )

    # =====================================================
    # SELECT OUR TEAMS
    # =====================================================

    target_teams = [
        "McLaren Mercedes",
        "McLaren",
        "Mercedes"
    ]

    selected_df = final_df[
        final_df["Team"].isin(target_teams)
    ].copy()

    # =====================================================
    # DISPLAY RESULTS
    # =====================================================

    print("\n================================")
    print("PERFORMANCE DATA")
    print("================================")

    print(
        selected_df.to_string(index=False)
    )

    # =====================================================
    # SAVE COMPLETE DATA
    # =====================================================

    final_df.to_csv(
        "f1_team_standings_raw.csv",
        index=False
    )

    # =====================================================
    # SAVE ONLY OUR TEAMS
    # =====================================================

    selected_df.to_csv(
        "f1_performance_raw.csv",
        index=False
    )

    print("\n================================")
    print("SCRAPING COMPLETED")
    print("================================")

    print(
        "\nTotal teams scraped:",
        len(final_df)
    )

    print(
        "Selected performance rows:",
        len(selected_df)
    )

    print("\nFiles saved:")

    print("f1_team_standings_raw.csv")
    print("f1_performance_raw.csv")

else:

    print("\nNo data was scraped.")
    