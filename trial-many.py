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
        return []

    time.sleep(2)
    soup = BeautifulSoup(page.text, 'html.parser')
    reviews = soup.find_all('div', class_='a-section review')
    products_names = soup.find_all('', 
    
    data = []
    for review in reviews:
        name = review.find('span', class_='a-profile-name').text.strip()
        rating = review.find('span', class_='a-icon-alt').text.strip()
        title = review.find('a', class_='a-size-base a-link-normal review-title a-color-base review-title-content a-text-bold').text.strip()
        body = review.find('span', class_='a-size-base review-text review-text-content').text.strip()
        data.append([name, rating, title, body])

    return data

amazon_url = 'https://www.amazon.in/Apple-iPhone-11-Pro-256GB/product-reviews/B07XVMJF2D/ref=cm_cr_dp_d_show_all_btm?ie=UTF8&reviewerType=all_reviews'
amazon_class = 'a-size-base'
amazon_data = get_data(amazon_url, amazon_class)

for i in amazon_data:
    print(i)
    print("\n")

headers = ['Name', 'Rating', 'Title', 'Body']
table = [
    ['Amazon Reviews', *headers],
    *amazon_data
]
print(tabulate(table, headers='firstrow', tablefmt='grid'))
