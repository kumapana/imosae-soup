from urllib import request
from bs4 import BeautifulSoup as BS


def main():
    url = "http://imotosae.com/news/"
    req = request.Request(url)
    res = request.urlopen(req)
    html = res.read()
    soup = BS(html, "lxml")
    print(soup)
    topics = soup.find_all('h1', 'c-thumb-index__title')
    for i in range(len(topics)):
        print(topics[i].string, "\n")


if __name__ == '__main__':
    main()
