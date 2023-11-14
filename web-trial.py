#!/usr/bin/python3
import sys
import time
from bs4 import BeautifulSoup
import requests
from tabulate import tabulate

def get_data(url, class_name):
    try:
        page = requests.get(url)
    except Exception as e:
        error_type, error_obj, error_info = sys.exc_info()
        print('ERROR FOR LINK:', url)
        print(error_type, 'Line:', error_info.tb_lineno)

    time.sleep(2)
    soup = BeautifulSoup(page.text, 'html.parser')
    links = soup.find_all('div', attrs={'class': 'a-size-base'})
    return [i.text.strip() for i in links]

amazon_url = 'https://www.amazon.in/Apple-iPhone-11-Pro-256GB/product-reviews/B07XVMJF2D/ref=cm_cr_dp_d_show_all_btm?ie=UTF8&reviewerType=all_reviews'
amazon_class = 'a-size-base'
amazon_data = get_data(amazon_url, amazon_class)

for i in amazon_data:
    print(i)
    print("\n")
table = [
    ['Amazon Reviews', *amazon_data]
]
print(tabulate(table, headers='firstrow', tablefmt='grid'))
