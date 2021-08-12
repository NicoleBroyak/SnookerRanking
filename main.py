from bs4 import BeautifulSoup
import requests


def ranking_get():
    url = "https://livescores.worldsnookerdata.com/Rankings/Index/14463"
    page = requests.get(url)
    return page


def ranking_parser(page):
    soup = BeautifulSoup(page.content, "html.parser")
    return soup


def scrape_table(soup):
    ths = soup.find_all("th")
    tds = soup.find_all("td")
    return ths + tds


def create_elements_list():
    elems = []
    for items in content:
        elems.append(items.text.strip())
    return elems


def write_elem_to_csv():
    length = 0
    file = open("Ranking.csv", "w")
    file.write("")
    file.close()
    file = open("Ranking.csv", "a")
    for count in range(0, len(elements)):
        file.write(elements[count] + ";")
        length += len(elements[count]) + 1
        if not (count + 1) % 5:
            file.truncate(length - 1)
            file.write("\n")
        count += 1
    file.close()


def repl_commas():
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


ranking_page = ranking_get()
parser = ranking_parser(ranking_page)
content = scrape_table(parser)
elements = create_elements_list()
write_elem_to_csv()
repl_commas()
