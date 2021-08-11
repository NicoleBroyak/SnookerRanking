from bs4 import BeautifulSoup
import requests


def ranking_update():
    file = open("Ranking.csv", "w")
    file.write("")
    file.close()
    url = "https://livescores.worldsnookerdata.com/Rankings/Index/14463"
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    ths = soup.find_all("th")
    tds = soup.find_all("td")
    length1 = 0
    for th in ths:
        soup.find("th")
        length = len(th.text.strip()) + 1
        file = open("Ranking.csv", "a")
        file.write(th.text.strip() + ";")
        length1 += length
    file.truncate(length1 - 1)
    file.write("\n")
    count = 0
    for td in tds:
        soup.find("td")
        length = len(td.text.strip()) + 1
        file = open("Ranking.csv", "a")
        file.write(td.text.strip() + ";")
        length1 += length
        count += 1
        if count == 5:
            file = open("Ranking.csv", "a")
            file.truncate(length1 - 1)
            file.write("\n")
            count = 0
    print("Ranking update finished")
    file = open("Ranking.csv")
    rep = file.read().replace(",", "")
    file.close()
    file = open("Ranking.csv", "w")
    file.write(rep)
    file.close()
    file = open("Ranking.csv")
    rep = file.read().replace(";", ",")
    file.close()
    file = open("Ranking.csv", "w")
    file.write(rep)
    file.close()


ranking_update()
