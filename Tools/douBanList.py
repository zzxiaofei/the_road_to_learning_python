import requests
from bs4 import BeautifulSoup
import os
import re
import pandas as pd

# import urllib3
# from urllib3.exceptions import HTTPError
#
# http = urllib3.PoolManager()
#
# try:
#     response = http.request('GET','https://book.douban.com/subject/35548280/')
#     print(response.data.decode('utf-8'))
#
# except HTTPError as e:
#     print(e.reason)


# 定义headers
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36'
}

# Target URL
urls = ['https://book.douban.com/people/79525026/wish']


# with open('urls.txt', 'r') as file:
#     urls = [line.strip() for line in file]

# Initialize the data
# books_data = []

def get_url_content(urls):
    book_url_list = []
    for url in urls:
        try:
            response = requests.get(url, headers=headers)
            if response.status_code == 200:
                soup = BeautifulSoup(response.text, 'html.parser')
                book_url = soup.find_all('div', class_='info')

                for book_item in book_url:
                    book_detail_url = book_item.find('a').get('href')
                    # book_detail_url = book_item.find_all('a')[0].get('href')
                    if book_detail_url.startswith('https://'):
                        print(book_detail_url)
                        book_url_list.append(book_detail_url)
        except Exception as e:
            print(f"A error occurred while accessing the current {url}: {e}")
    with open('MyBookList.txt', 'w') as file:
        for link in book_url_list:
            file.write(link + '\n')
    print("All Done")

if __name__ == '__main__':
    get_url_content(urls)