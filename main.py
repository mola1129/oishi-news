import cloudinary
import cloudinary.uploader
import requests
import news.api as news_api
import line.notify as line
import os

# 記事のURLを取得
new_news = news_api.get_oishi()

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
    type="upload", resource_type="raw", prefix="oishi-news/")
file_url = res["resources"][0]["secure_url"]
headers = {"content-type": "application/json"}
# news.jsonを取得
r = requests.get(file_url, headers=headers)
old_news = r.json()["news"]

# 記事の差分を抽出
diff_news = news_api.get_diff(new_news, old_news)

# Line Messaging APIで通知
line_token = os.environ['LINE_TOKEN']
if diff_news != []:
    for news in diff_news:
        message = news["title"] + '\n' + news["url"] + '\n\n'
        line.post_line_message(line_token, message)

# 今回取得した記事一覧をcloudinaryに保存
news_api.upload('news.json', new_news)
