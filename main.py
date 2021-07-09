from bs4 import BeautifulSoup
from urllib import request

import xml.etree.ElementTree as ET


def main() -> None:
    url: str = "https://www.aozora.gr.jp/cards/001475/files/53453_50584.html"
    scrape(url)


def scrape(url: str) -> None:
    response = request.urlopen(url)
    soup = BeautifulSoup(response)
    response.close()
    main_text = soup.find('div', class_='main_text')
    f = open('main_text.xml', 'w')
    f.write(main_text.__str__())
    f.close()
