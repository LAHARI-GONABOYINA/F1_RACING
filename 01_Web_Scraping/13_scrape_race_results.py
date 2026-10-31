import requests
from bs4 import BeautifulSoup
import pandas as pd


# =========================================================
# SCRAPE RACE WINNERS
# =========================================================

def scrape_race_winners(season):

    print(f"\nScraping {season} race results...")

    url = f"https://www.formula1.com/en/results/{season}/races"

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
        print("No race results table found.")
        return None

    rows = table.find_all("tr")

    data = []

    for row in rows:

        cells = row.find_all(["th", "td"])

        values = [
            cell.get_text(" ", strip=True)
            for cell in cells
        ]

        if len(values) == 6:

            # Skip header
            if values[0] == "Grand Prix":
                continue

            data.append([
                season,
                values[0],
                values[1],
                values[2],
                values[3],
                values[4],
                values[5]
            ])

    df = pd.DataFrame(
        data,
        columns=[
            "Season",
            "Grand_Prix",
            "Date",
            "Winner",
            "Team",
            "Laps",
            "Time"
        ]
    )

    print("Races scraped:", len(df))

    return df


# =========================================================
# SCRAPE 2024
# =========================================================

df_2024 = scrape_race_winners(2024)


# =========================================================
# SCRAPE 2025
# =========================================================

df_2025 = scrape_race_winners(2025)


# =========================================================
# COMBINE
# =========================================================

dataframes = []

if df_2024 is not None:
    dataframes.append(df_2024)

if df_2025 is not None:
    dataframes.append(df_2025)


if not dataframes:

    print("\nNo data was scraped.")

else:

    race_df = pd.concat(
        dataframes,
        ignore_index=True
    )

    # =====================================================
    # SAVE RAW RACE DATA
    # =====================================================

    race_df.to_csv(
        "f1_race_results_raw.csv",
        index=False
    )

    print("\nRaw race data saved:")
    print("f1_race_results_raw.csv")


    # =====================================================
    # CALCULATE WINS
    # =====================================================

    target_teams = [
        "McLaren Mercedes",
        "McLaren",
        "Mercedes"
    ]

    selected_races = race_df[
        race_df["Team"].isin(target_teams)
    ].copy()


    # Count wins by season and team

    wins = (
        selected_races
        .groupby(["Season", "Team"])
        .size()
        .reset_index(name="Wins")
    )


    # =====================================================
    # DISPLAY WINNING RACES
    # =====================================================

    print("\n================================")
    print("WINNING RACES")
    print("================================")

    if len(selected_races) > 0:

        print(
            selected_races[
                [
                    "Season",
                    "Grand_Prix",
                    "Winner",
                    "Team"
                ]
            ].to_string(index=False)
        )

    else:

        print("No McLaren or Mercedes wins found.")


    # =====================================================
    # DISPLAY WIN SUMMARY
    # =====================================================

    print("\n================================")
    print("WIN SUMMARY")
    print("================================")

    print(
        wins.to_string(index=False)
    )


    # =====================================================
    # SAVE WIN DATA
    # =====================================================

    wins.to_csv(
        "f1_team_wins.csv",
        index=False
    )


    print("\n================================")
    print("RACE RESULT SCRAPING COMPLETED")
    print("================================")

    print("\nFiles created:")

    print("f1_race_results_raw.csv")
    print("f1_team_wins.csv")