from bs4 import BeautifulSoup as BS4
from urllib import request

#import xml.etree.ElementTree as ET


def main() -> None:
    #url: str = "https://www.aozora.gr.jp/cards/001475/files/53453_50584.html"
    library_card_url: str = "https://www.aozora.gr.jp/cards/000879/card4872.html"
    scrape_library_card(library_card_url)


def scrape_library_card(url: str) -> None:
    response = request.urlopen(url)
    soup = BS4(response, 'html.parser')
    response.close()

    buffer = [
        element for div in soup('div', align='right')
        for element in div('a')
    ]

    for element in buffer:
        print(element)
        print(element('href'))

    print(url)

    # def scrape(url: str) -> None:
    #    response = request.urlopen(url)
    #    soup = BeautifulSoup(response)
    #    response.close()
    #    main_text = soup.find('div', class_='main_text')
    #    f = open('main_text.xml', 'w')
    #    f.write(main_text.__str__())
    #    f.close()


if __name__ == "__main__":
    main()
