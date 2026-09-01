import urllib.request
import xml.etree.ElementTree as ET

def get_latest_blog_post():
    rss_feed_url = "https://nube.codeberg.page/blog/index.xml"
    req = urllib.request.Request(
        rss_feed_url, 
        headers={'User-Agent': 'Mozilla/5.0'}
    )
    with urllib.request.urlopen(req) as response:
        xml_data = response.read()
    
    root = ET.fromstring(xml_data)
    item = root.find('.//channel/item')
    
    title = item.find('title').text
    link = item.find('link').text
    return title, link

if __name__ == "__main__":
    title, link = get_latest_blog_post()
    print(f"[{title}]({link})")
