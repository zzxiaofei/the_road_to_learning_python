import requests
from bs4 import BeautifulSoup
import os
import re
import pandas as pd
from douBanList import get_url_content
import logging
from concurrent.futures import ThreadPoolExecutor, as_completed



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


# Define headers
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 '
                  'Safari/537.36'
}

# Target URL
Multi_urls = ['https://book.douban.com/subject/26061406/', 'https://book.douban.com/subject/6971390/']


def fetch_urls_from_txt(url):
    with open('MyBookList.txt', 'r') as file:
        mass_urls = [line.strip() for line in file]


def fetch_page(url, header):
    try:
        # Send GET Request
        response = requests.get(url, headers=headers)
        # Check HTTP Response Code
        response.raise_for_status()
        # Parsing HTML
        return BeautifulSoup(response.text, 'html.parser')
    except requests.requestException as e:
        print(f"Error while fetching {url}: {e}")
        return None
def parse_html(soup):
    # Initialize the data
    books_info = {}
    # Find all the <div> tags meet the criteria
    # book_list = soup.find_all('div', class_='info')

    # Check Author Info
    book_author = soup.find('meta', attrs={'property': 'book:author'})
    books_info['author'] = book_author['content'] if book_author and 'content' in book_author.attrs else None

    # Check Image Link

    # Find all the <a> tags that meet the criteria
    image_links = soup.find_all('a', class_='nbg')
    books_info['image_links'] = [link.get('href') for link in image_links]
    books_info['title'] = [re.sub(r'[\\/*?:"<>|]', "", link.get("title", "") for link in image_links]

    return books_info

def download_images(image_url, title):
    try:
        image_response = requests.get(image_url)
        image_response.raise_for_status()

        if not os.path.exists('doubanCover_images'):
            os.makedirs('doubanCover_images')
        # Extracting image name
        image_name = f"doubanCover_images/{title}.jpg"
        # Image saving Path
        image_path = os.path.join('doubanCover_images', image_name)
        with open(image_name, 'wb') as f:
            f.write(image_response.content)
        print(f"Already downloaded the image {title}")
    except requests.RequestException as e:
        logging.error(f"Error while downloading image {title} from {image_url}: {e}")


            if title and author:
                books_data.append({'title': title, 'author': author, 'url': url})
                print(f"Added book {title}, {author} and {url}")
        else:
            print(f"failed to retrieve image from {url}")
    except Exception as e:
        print(f"A error occurred while accessing the current {url}: {e}")
df = pd.DataFrame(books_data)
df.to_excel('douban_books.xlsx', index=False, engine='openpyxl')
print("Done!")
