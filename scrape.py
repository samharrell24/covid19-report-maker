from bs4 import BeautifulSoup
import requests

f = open("output/data.txt", "w")
page = requests.get("https://www.worldometers.info/coronavirus/")

if page.status_code == 200:
    soup = BeautifulSoup(page.content, 'html.parser')
    table = soup.find(id="main_table_countries_today")
    f.write(str(table.find("tbody")))
