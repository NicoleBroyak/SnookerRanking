from bs4 import BeautifulSoup
import requests
import pathlib
import logging


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

def write_elems_to_csv():
    length = 0
    file_path = pathlib.Path("Ranking.csv")
    try:
        with file_path.open(mode="w") as file:
            file.write("")
    except OSError:
        logging.error("Error11")
    try:
        with file_path.open(mode="a") as file:
            for count in range(0, len(elements)):
                file.write(elements[count] + ";")
                length += len(elements[count]) + 1
                if not (count + 1) % 5:
                    file.truncate(length - 1)
                    file.write("\n")
                count += 1
    except OSError:
        logging.error("Error")


def repl_commas():
    file_path = pathlib.Path("Ranking.csv")
    try:
        with file_path.open() as file:
            rep = file.read().replace(",", "")
    except OSError:
        logging.error("Error")
    try:
        with file_path.open(mode="w") as file:
            file.write(rep)
    except OSError:
        logging.error("Error")
    try:
        with file_path.open() as file:
            rep = file.read().replace(";", ",")
    except OSError:
        logging.error("Error")
    try:
        with file_path.open(mode="w") as file:
            file.write(rep)
    except OSError:
        logging.error("Error")


ranking_page = ranking_get()
parser = ranking_parser(ranking_page)
content = scrape_table(parser)
elements = create_elements_list()
write_elems_to_csv()
repl_commas()
