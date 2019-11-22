import requests


# LINE Notify に通知する
def post_line_notify(token, message):
    # LINE Notify API URL
    url = 'https://notify-api.line.me/api/notify'

    # リクエストパラメータ
    headers = {'Authorization': 'Bearer {0}'.format(token)}
    payload = {}
    # メッセージ追加
    if message:
        payload["message"] = message
    try:
        requests.post(url, headers=headers, params=payload)
    except Exception as e:
        raise e
