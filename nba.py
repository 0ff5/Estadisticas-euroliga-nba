import requests
from bs4 import BeautifulSoup

first_name = input("Ingrese el nombre(SIN APELLIDO O SEGUNDO NOMBRE) del jugador: ")
last_name = input("Apellido: ")

url = "https://givemestats.com/basketball-player-stats-gamelogs.php?player=" + first_name + "%20" + last_name

response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")

stats = soup.find_all("div", class_="player-stats-cells-label")

for stat in stats:
    text = stat.next_sibling.string.strip()
    if stat.text in ["MIN", "PTS", "REB", "AST", "INX"]:
        print("{}: {}".format(stat.text, text))