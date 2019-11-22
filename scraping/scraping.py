import requests
import bs4


def get_news_urls_from_oishi():
    url = 'https://www.014014.jp/news'
    response = requests.get(url)
    soup = bs4.BeautifulSoup(response.text, 'lxml')
    news = soup.select("div > ul > li > p > a")
    urls = []
    for n in news:
        urls.append(n.get('href'))
    return urls
