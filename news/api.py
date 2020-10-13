import cloudinary.uploader
import json
import requests
import bs4


def get_oishi():
    url = 'https://www.014014.jp/news'
    response = requests.get(url)
    soup = bs4.BeautifulSoup(response.text, 'lxml')

    # 記事の<a>タグを取得
    links = soup.select("div > ul > li > p > a")
    news_list = []
    n = len(links)
    for i in range(n):
        # タイトルとURLを追加
        title = links[i].get_text()
        url = links[i].get('href')
        news_list.append({
            title,
            url,
        })
    return news_list


def get_diff(new_news, old_news):
    diff_news = []
    for news in new_news:
        if not (news in old_news):
            diff_news.append(news)
    return diff_news


def upload(filename, news):
    # dictの内容をjsonとしてローカル保存
    with open(filename, 'w') as f:
        json.dump({news}, f, indent=4)

    # 保存ファイルをcloudinaryへアップロード
    cloudinary.uploader.upload(
        file=filename, folder="oishi-news/", use_filename=True,
        unique_filename=False, resource_type="raw",
    )