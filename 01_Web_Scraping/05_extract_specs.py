import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://www.mclaren.com/racing/formula-1/2024/mclaren-mcl38-technical-specification/"

response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

table = soup.find("table")

rows = table.find_all("tr")

data = []

for row in rows:
    cells = row.find_all(["th", "td"])
    
    values = [cell.get_text(" ", strip=True) for cell in cells]
    
    if values:
        data.append(values)

df = pd.DataFrame(data, columns=["Specification", "Value"])

print(df)