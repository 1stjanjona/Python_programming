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
    reviews = soup.find_all('div', class_='a-section review')

    amazon_data = []

    for review in reviews:
        product_name_tag = review.find('a', class_='a-size-base a-link-normal review-title a-color-base review-title-content a-text-bold')
        rating_tag = review.find('span', class_='a-icon-alt')
        title_tag = review.find('span', class_='a-size-base review-text review-text-content')
        price_tag = review.find('span', class_='a-offscreen')
        recommendation_tag = review.find('span', class_='a-size-mini a-color-state a-text-bold')
        num_purchases_tag = review.find('span', class_='a-size-base a-color-tertiary')

        if product_name_tag:
            product_name = product_name_tag.text.strip()
        else:
            product_name = ''

        if rating_tag:
            rating = rating_tag.text.strip()
        else:
            rating = ''

        if title_tag:
            title = title_tag.text.strip()
        else:
            title = ''

        if price_tag:
            price = price_tag.text.strip()
        else:
            price = ''

        if recommendation_tag:
            recommendation = recommendation_tag.text.strip()
        else:
            recommendation = ''

        if num_purchases_tag:
            num_purchases = num_purchases_tag.text.strip()
        else:
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
