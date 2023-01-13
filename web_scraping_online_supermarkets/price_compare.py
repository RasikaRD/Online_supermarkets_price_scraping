import requests
import json
import sys

sys.path.insert(0, 'bs4.zip')

from bs4 import BeautifulSoup

# Imitate the Mozilla browser.
user_agent = {'User-agent': 'Mozilla/5.0'}


def compare_prices(product_laughs, product_glomark):
    # TODO: Aquire the web pages which contain product Price

    response1 = requests.get(product_laughs, headers=user_agent)
    response2 = requests.get(product_glomark, headers=user_agent)

    # TODO: LaughsSuper supermarket website provides the price in a span text.

    soup1 = BeautifulSoup(response1.content, 'html.parser')
    product_name_laughs = soup1.find('div', class_="product-name").get_text().strip()
    pl = soup1.find('span', class_="regular-price").get_text().strip()
    price_laughs = float(pl[3:-2])

    # TODO: Glomark supermarket website provides the data in jason format in an inline script.
    # You can use the json module to extract only the price
    soup2 = BeautifulSoup(response2.content, 'html.parser')
    product_name_glomark = soup2.find('div', class_="product-title").get_text().strip()
    script = soup2.find('script', type='application/ld+json').text.strip()
    data = json.loads(script)
    pk = data['offers'][0]['price']
    price_glomark = float(pk)

    # TODO: Parse the values as floats, and print them.

    print('Laughs  ', product_name_laughs, 'Rs.: ', price_laughs)
    print('Glomark ', product_name_glomark, 'Rs.: ', price_glomark)

    if (price_laughs > price_glomark):
        print('Glomark is cheaper Rs.:', price_laughs - price_glomark)
    elif (price_laughs < price_glomark):
        print('Laughs is cheaper Rs.:', price_glomark - price_laughs)
    else:
        print('Price is the same')
