import os

import requests
import pandas as pd
from bs4 import BeautifulSoup
from datetime import datetime
from urllib.parse import quote

BASE_URL = "https://www.imot.bg/pcgi/imot.cgi?act=14"

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
    "AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/120.0.0.0 "
    "Safari/537.36"
}

response = requests.get(BASE_URL, headers=HEADERS)
response.encoding = "windows-1251"

soup = BeautifulSoup(response.text, "html.parser")

city_select = soup.find("select", {"name": "town"})
cities = (
    {option.text.strip(): option["value"] for option in city_select.find_all("option")}
    if city_select
    else {}
)

current_year = datetime.today().year
current_date = datetime.today().strftime("%d.%m.%Y")

all_data = []

for city_name, city_value in cities.items():
    encoded_city = quote(city_value, encoding="windows-1251")
    city_url = (
        f"https://www.imot.bg/pcgi/imot.cgi?act=14&pn=0&town="
        f"{encoded_city}&year={current_year}&date={current_date}"
    )
    response = requests.get(city_url, headers=HEADERS)
    response.encoding = "windows-1251"
    soup = BeautifulSoup(response.text, "html.parser")
    table = soup.find("table", {"id": "tableStats", "class": "tabStat"})

    if table:
        rows = table.find_all("tr")[2:]

        for row in rows:
            columns = [
                td.text.strip().replace("\xa0", "").replace(",", "")
                for td in row.find_all("td")
                if td.text.strip() != ""
            ]

            if len(columns) >= 7:
                district_name = columns[0]
                one_bedroom_price = columns[1]
                one_bedroom_price_per_m2 = columns[2]
                two_bedroom_price = columns[3]
                two_bedroom_price_per_m2 = columns[4]
                three_bedroom_price = columns[5]
                three_bedroom_price_per_m2 = columns[6]

                link_tag = row.find("a")
                link = "https://www.imot.bg/" + link_tag["href"] if link_tag else "N/A"

                all_data.append(
                    [
                        current_date,
                        city_value,
                        district_name,
                        one_bedroom_price,
                        one_bedroom_price_per_m2,
                        two_bedroom_price,
                        two_bedroom_price_per_m2,
                        three_bedroom_price,
                        three_bedroom_price_per_m2,
                        link,
                    ]
                )

    else:
        print(f" No data found for {city_value}")

df = pd.DataFrame(
    all_data,
    columns=[
        "Date",
        "City",
        "District",
        "One_Bedroom_Price-(euro)",
        "One_Bedroom_Price_Per_m2-(euro)",
        "Two_Bedroom_Price-(euro)",
        "Two_Bedroom_Price_Per_m2-(euro)",
        "Three_Bedroom_Price-(euro)",
        "Three_Bedroom_Price_Per_m2-(euro)",
        "Link",
    ],
)

save_directory = "/Users/krumyakimov/Documents/simple_django_projects/RealEstateData"
os.makedirs(save_directory, exist_ok=True)

filename = os.path.join(save_directory, f"real_estate_prices_{current_date}.csv")
df.to_csv(filename, index=False, encoding="utf-8-sig")

print(f"Data saved in a single file: {filename}")
