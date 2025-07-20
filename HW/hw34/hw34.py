import csv
from bs4 import BeautifulSoup
import requests


def get_html(url):
    row = requests.get(url)
    return row.text


def get_data(html):
    soup = BeautifulSoup(html, "lxml")
    horoscope = soup.find_all("article", class_="IGRa5")

    for cont in horoscope:
        sign = cont.find("h3", class_="_4K6U+").text
        data_sign = cont.find("p", class_="vpvdP").text
        card = cont.find("div", class_="BDPZt").text
        data = {
            "sign": sign,
            "data_sign": data_sign,
            "card": card,
        }
        write_csv(data)


def write_csv(data):
    with open("hw34.csv", "a") as f:
        writer = csv.writer(f, delimiter=";", lineterminator="\r")
        writer.writerow((data["sign"], data["data_sign"], data["card"]))


def main():
    url = "https://72.ru/horoscope/daily/"
    get_data(get_html(url))


if __name__ == '__main__':
    main()



# row = requests.get("https://72.ru/horoscope/weekly/")
# print(row)