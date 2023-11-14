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
    links = soup.find_all('div', attrs={'class': class_name})
    return [i.text.strip() for i in links]
cricbuzz_url = 'https://www.cricbuzz.com/'
cricbuzz_class = 'cb-nws-intr'
cricbuzz_data = get_data(cricbuzz_url, cricbuzz_class)
for i in cricbuzz_data:
    print(i)
    print("\n")
table = [
    ['Cricbuzz News', *cricbuzz_data]
]
print(tabulate(table, headers='firstrow', tablefmt='grid'))
