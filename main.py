import cloudinary
import cloudinary.uploader
import requests
import scraping.scraping as sc
import urldata.setup as url
import line.notify as line
import os

# 記事のURLを取得
news_urls = sc.get_news_urls_from_oishi()

cloud_name = os.environ['CLOUD_NAME']
api_key = os.environ['API_KEY']
api_secret = os.environ['API_SECRET']
cloudinary.config(
    cloud_name=cloud_name,
    api_key=api_key,
    api_secret=api_secret
)
# 前回の記事URLを取得
res = cloudinary.api.resources(
    type="upload", resource_type="raw", prefix="oishi-news")
file_url = res["resources"][0]["secure_url"]
r = requests.get(file_url)
with open('urls.txt', mode='w') as f:
    f.write(r.text)

# 記事の差分を抽出
diff = url.get_diff_urls(news_urls, 'urls.txt')
url.save_urls('urls.txt', news_urls)

# Line Messaging APIで通知
line_token = os.environ['LINE_TOKEN']
if diff != []:
    message = '\n'
    for d in diff:
        message += d + '\n\n'
    line.post_line_message(line_token,message)
