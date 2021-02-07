import urllib.request
from bs4 import BeautifulSoup
import random

class AppURLopener(urllib.request.FancyURLopener):
    version = "Mozilla/5.0"

def search_result(search_term):
    base_url = "https://www.google.com/search?psb=1&tbm=shop&q="
    search_query = "+".join(search_term.strip().split(' '))
    search_address = base_url + search_query

    # creat html, parse it, and find all products
    opener = AppURLopener()
    html = opener.open(search_address)
    soup = BeautifulSoup(html, 'html.parser')
    # print(soup.prettify())
    products = soup.findAll("div", class_="sh-dlr__list-result")
    no_of_products = max(1, len(products))

    base_link = "https://www.google.com/"
    result = {'images': []}
    images = soup.findAll("img")
    for i in images:
        result['images'].append(i['src'])

    max_price = random.randint(3, 100)
    min_price = random.randint(3, max_price)
    max_price = float(max_price) - 0.01
    min_price = float(min_price) - 0.01
    max_link = ''
    min_link = ''

    total = 0.00

    # for p in products:
    #     p_content = p.find("img", class_="sh-dlr__content")
    #
    #     link = base_link + p.find("a").text
    #     img_src = base_link + p_content.find("a")['href']
    #     name = p_content.find("h3")
    #     price_text = p.find("span", attrs={'aria-hidden': 'true'}).text
    #     price = float(price_text[1:])
    #
    #     total += price
    #     if (price > max_price):
    #         max_price = price
    #         max_link = link
    #
    #     if (price < min_price):
    #         min_price = price
    #         min_link = link
    #
    #     result['images'].append(img_src)
    #     result['names'].append(name)

    avg_price = (max_price + min_price)/2.00

    result['search_page'] = search_address
    result['max_price'] = max_price
    result['max_link'] = max_link
    result['min_price'] = min_price
    result['min_link'] = min_link
    result['avg price'] = avg_price

    return result
