import requests
from bs4 import BeautifulSoup
import pandas as pd
import re
import time


HEADERS = {
    "User-Agent": "Mozilla/5.0"
}


# =========================================================
# GET 2024/2025 RACE LINKS
# =========================================================

def get_race_links(season):

    print(f"\nFinding {season} race links...")

    url = f"https://www.formula1.com/en/results/{season}/races"

    response = requests.get(
        url,
        headers=HEADERS,
        timeout=20
    )

    print("Status code:", response.status_code)

    soup = BeautifulSoup(response.text, "html.parser")

    links = []

    for a in soup.find_all("a", href=True):

        href = a["href"]

        if f"/results/{season}/" in href:

            if href not in links:
                links.append(href)

    print("Race links found:", len(links))

    return links


# =========================================================
# EXTRACT PODIUM FROM A RACE PAGE
# =========================================================

def scrape_podium(url, season):

    response = requests.get(
        url,
        headers=HEADERS,
        timeout=20
    )

    if response.status_code != 200:
        return []

    soup = BeautifulSoup(response.text, "html.parser")

    table = soup.find("table")

    if table is None:
        return []

    rows = table.find_all("tr")

    podium = []

    for row in rows:

        cells = row.find_all(["th", "td"])

        values = [
            cell.get_text(" ", strip=True)
            for cell in cells
        ]

        if len(values) >= 3:

            position = values[0]

            if position in ["1", "2", "3"]:

                podium.append({
                    "Season": season,
                    "Position": int(position),
                    "Driver": values[1],
                    "Team": values[2]
                })

    return podium


# =========================================================
# MAIN SCRAPER
# =========================================================

all_podiums = []


for season in [2024, 2025]:

    race_links = get_race_links(season)

    for i, link in enumerate(race_links):

        # Convert relative URL to full URL
        if link.startswith("/"):
            full_url = "https://www.formula1.com" + link
        else:
            full_url = link

        print(
            f"Processing {season} race {i + 1}/{len(race_links)}"
        )

        podium = scrape_podium(
            full_url,
            season
        )

        all_podiums.extend(podium)

        time.sleep(0.5)


# =========================================================
# CREATE DATAFRAME
# =========================================================

df = pd.DataFrame(all_podiums)


print("\n================================")
print("PODIUM EXTRACTION")
print("================================")

print("Total podium records:", len(df))

if len(df) > 0:

    print(
        df.to_string(index=False)
    )

    # -----------------------------------------------------
    # SELECT McLAREN AND MERCEDES
    # -----------------------------------------------------

    target_teams = [
        "McLaren",
        "McLaren Mercedes",
        "Mercedes"
    ]

    selected = df[
        df["Team"].isin(target_teams)
    ].copy()


    # -----------------------------------------------------
    # DISPLAY SELECTED PODIUMS
    # -----------------------------------------------------

    print("\n================================")
    print("McLAREN / MERCEDES PODIUMS")
    print("================================")

    print(
        selected.to_string(index=False)
    )


    # -----------------------------------------------------
    # COUNT PODIUMS
    # -----------------------------------------------------

    podium_summary = (
        selected
        .groupby(["Season", "Team"])
        .size()
        .reset_index(name="Podiums")
    )


    print("\n================================")
    print("PODIUM SUMMARY")
    print("================================")

    print(
        podium_summary.to_string(index=False)
    )


    # -----------------------------------------------------
    # SAVE FILES
    # -----------------------------------------------------

    df.to_csv(
        "f1_podium_results_raw.csv",
        index=False
    )

    podium_summary.to_csv(
        "f1_team_podiums.csv",
        index=False
    )


    print("\n================================")
    print("PODIUM SCRAPING COMPLETED")
    print("================================")

    print("\nFiles created:")
    print("f1_podium_results_raw.csv")
    print("f1_team_podiums.csv")

else:

    print("\nNo podium data found.")