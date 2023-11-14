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

    amazon_data = []

    for review in reviews:
        try:
            product_name = review.find('a', class_='a-size-base a-link-normal review-title a-color-base review-title-content a-text-bold').text.strip()
        except AttributeError:
            product_name = ''

        try:
            rating = review.find('span', class_='a-icon-alt').text.strip()
        except AttributeError:
            rating = ''

        try:
            title = review.find('span', class_='a-size-base review-text review-text-content').text.strip()
        except AttributeError:
            title = ''

        try:
            price = review.find('span', class_='a-offscreen').text.strip()
        except AttributeError:
            price = ''

        try:
            recommendation = review.find('span', class_='a-size-mini a-color-state a-text-bold').text.strip()
        except AttributeError:
            recommendation = ''

        try:
            num_purchases = review.find('span', class_='a-size-base a-color-tertiary').text.strip()
        except AttributeError:
            num_purchases = ''

        amazon_data.append({
            'Name': product_name,
            'Rating': rating,
            'Title': title,
            'Price': price,
            'Recommendation': recommendation,
            'Number of Purchases': num_purchases,
        })

    return amazon_data

amazon_url = 'https://www.amazon.in/Apple-iPhone-11-Pro-256GB/product-reviews/B07XVMJF2D/ref=cm_cr_dp_d_show_all_btm?ie=UTF8&reviewerType=all_reviews'
amazon_class = 'a-size-base'
amazon_data = get_data(amazon_url, amazon_class)

# Create a table
table = tabulate(amazon_data, headers='keys', tablefmt='grid')
print(table)
