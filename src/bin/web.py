import httpx
from selectolax.parser import HTMLParser


def get_html():
    url = ""
    headers = {}

    resp = httpx.get(url, headers = headers)
    html = HTMLParser(resp.text)
    return html

def extract_text(html, sel):
    try:
        return html.css_first(sel).text()
    except AttributeError:
        return None


def parse_page(html):
    products = html.css("")
    
    for product in products:
        item = {}
        print(item)


def main():
    html = get_html()
    parse_page(html)

if __name__ == "__main__":
    main()
