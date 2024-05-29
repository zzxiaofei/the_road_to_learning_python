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
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 '
                  'Safari/537.36'
}

# Target URL
urls = ['https://book.douban.com/subject/26061406/', 'https://book.douban.com/subject/6971390/']

# with open('urls.txt', 'r') as file:
#     urls = [line.strip() for line in file]

# Initialize the data
# books_data = []

for url in urls:
    try:
        # Send GET Request
        response = requests.get(url, headers=headers)

        # Check HTTP Response Code
        if response.status_code == 200:
            # Parsing HTML
            soup = BeautifulSoup(response.text, 'html.parser')

            # Find all the <div> tags meet the criteria
            # book_list = soup.find_all('div', class_='info')

            Book_author = soup.find('meta', attrs={'property': 'book:author'})

            if Book_author and 'content' in Book_author.attrs:
                author = Book_author['content']
                print(f'The author is: {author}')
            else:
                print("No author found")

            # Find all the <a> tags that meet the criteria
            image_links = soup.find_all('a', class_='nbg')

            # Check if there a link of image
            if not image_links:
                print('Image links not found.')
            else:
                # Create a folder to save the images
                if not os.path.exists('douban_images'):
                    os.makedirs('douban_images')

                # loop through each image link
                for idx, link in enumerate(image_links):
                    image_url = link.get("href")
                    title = link.get("title")
                    title = re.sub(r'[\\/*?:"<>|]', "", title)

                    # Download the image
                    image_response = requests.get(image_url)
                    if image_response.status_code == 200:
                        # Extracting image name
                        image_name = f"douban_images/{title}.png"
                        # Image saving Path
                        image_path = os.path.join('douban_images', image_name)
                        # Write to image file
                        with open(image_name, 'wb') as f:
                            f.write(image_response.content)
                        print(f"Already downloaded the image {title}")
                    else:
                        print(f"Could not retrieve image {title}")
            # for idx, book in enumerate(book_list):
            #     author = book.find('a')['title']

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
