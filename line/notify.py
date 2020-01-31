from linebot import LineBotApi
from linebot.models import TextSendMessage


# Messaging API でブロードキャスト送信する
def post_line_message(token, message):
    line_bot_api = LineBotApi(token)
    res = line_bot_api.broadcast(TextSendMessage(text=message))
