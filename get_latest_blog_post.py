import requests

def get_latest_blog_post():
    rss_feed_url = "https://nube.bearblog.dev/feed"
    response = requests.get(f"https://api.rss2json.com/v1/api.json?rss_url={rss_feed_url}")
    data = response.json()
    latest_post = data['items'][0]
    return latest_post['title'], latest_post['link']

if __name__ == "__main__":
    title, link = get_latest_blog_post()
    print(f"[{title}]({link})")