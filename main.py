import scraping.scraping as sc
import urldata.setup as url
import line.notify as line
import os

print(os.environ["HOME"])

urls = sc.get_news_urls_from_oishi()
diff = url.get_diff_urls(urls)
url.save_urls('urls.txt', urls)
line_token = os.environ['LINE_TOKEN']
if diff != []:
    message = '\n'
    for d in diff:
        message += d + '\n\n'
    line.post_line_notify(line_token, message)
