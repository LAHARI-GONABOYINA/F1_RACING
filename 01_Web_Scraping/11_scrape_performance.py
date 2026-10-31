import requests
from bs4 import BeautifulSoup
import pandas as pd


# =========================================================
# Scrape F1 Team Standings
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

    data = []

    # Find all tables
    tables = soup.find_all("table")

    print("Tables found:", len(tables))

    for table in tables:

        rows = table.find_all("tr")

        for row in rows:

            cells = row.find_all(["th", "td"])

            values = [
                cell.get_text(" ", strip=True)
                for cell in cells
            ]

            if values:
                print(values)

    return data


# =========================================================
# Scrape 2024
# =========================================================

scrape_team_standings(2024)


# =========================================================
# Scrape 2025
# =========================================================

scrape_team_standings(2025)