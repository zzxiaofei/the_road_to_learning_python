import requests  # 导入 requests 库，用于发送 HTTP 请求
from bs4 import BeautifulSoup  # 导入 BeautifulSoup 库，用于解析 HTML
import os  # 导入 os 模块，用于文件和目录操作
import re  # 导入 re 模块，用于正则表达式操作
import pandas as pd  # 导入 pandas 库，用于数据处理
import logging  # 导入 logging 模块，用于记录日志
from concurrent.futures import ThreadPoolExecutor, as_completed  # 导入线程池相关模块，用于并发处理
from douBanList import get_url_content

# 配置日志
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# 定义headers
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 '
                  'Safari/537.36'
}

# 定义文件路径
URLS_FILE = 'MyBookList.txt'  # URL 列表文件路径
IMAGE_DIR = 'douban_images'  # 图片保存目录路径
EXCEL_FILE = 'douban_books.xlsx'  # Excel 文件保存路径


def fetch_page(url, headers):
    try:
        response = requests.get(url, headers=headers)  # 发送 GET 请求
        response.raise_for_status()  # 检查响应状态码
        return BeautifulSoup(response.text, 'html.parser')  # 使用 BeautifulSoup 解析 HTML
    except requests.RequestException as e:
        logging.error(f"Error fetching {url}: {e}")  # 记录错误日志
        return None


def parse_book_info(soup):
    book_info = {}

    # 查找作者信息
    book_author = soup.find('meta', attrs={'property': 'book:author'})
    book_info['author'] = book_author['content'] if book_author and 'content' in book_author.attrs else None

    # 查找图片链接
    image_links = soup.find_all('a', class_='nbg')
    book_info['image_links'] = [link.get("href") for link in image_links]
    book_info['titles'] = [re.sub(r'[\\/*?:"<>|]', "", link.get("title", "")) for link in image_links]

    return book_info


def download_image(image_url, title):
    try:
        image_response = requests.get(image_url)  # 发送 GET 请求下载图片
        image_response.raise_for_status()  # 检查响应状态码
        image_name = os.path.join(IMAGE_DIR, f"{title}.png")  # 构建图片保存路径
        with open(image_name, 'wb') as f:
            f.write(image_response.content)  # 将图片内容写入文件
        logging.info(f"Downloaded image {title}")  # 记录下载成功的日志
    except requests.RequestException as e:
        logging.error(f"Error downloading image {title} from {image_url}: {e}")  # 记录下载失败的日志


def process_url(url):
    soup = fetch_page(url, HEADERS)  # 发送请求并解析页面
    if soup:
        book_info = parse_book_info(soup)  # 解析书籍信息
        author = book_info.get('author')
        image_links = book_info.get('image_links')
        titles = book_info.get('titles')

        books_data = []
        for title, image_url in zip(titles, image_links):
            if title and author:
                books_data.append({'title': title, 'author': author, 'url': url})  # 构建书籍信息列表
                download_image(image_url, title)  # 下载图片
                logging.info(f"Added book {title}, {author}, {url}")  # 记录添加书籍的日志
        return books_data
    return []


def process_urls_concurrently(urls, max_workers=5):
    books_data = []
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        future_to_url = {executor.submit(process_url, url): url for url in urls}  # 并发处理 URL 列表
        for future in as_completed(future_to_url):
            result = future.result()
            if result:
                books_data.extend(result)
    return books_data


def save_to_excel(data, filename):
    df = pd.DataFrame(data)
    df.to_excel(filename, index=False, engine='openpyxl')  # 将数据保存到 Excel 文件中
    logging.info(f"Data saved to {filename}")  # 记录保存成功的日志


def main():
    get_url_content(['https://book.douban.com/people/79525026/wish'])
    # 从urls.txt文件读取URL列表
    if os.path.exists(URLS_FILE):
        with open(URLS_FILE, 'r') as file:
            urls = [line.strip() for line in file]
    else:
        logging.error(f"URLs file {URLS_FILE} not found")  # 记录文件不存在的错误日志
        return

    # 创建图片目录
    if not os.path.exists(IMAGE_DIR):
        os.makedirs(IMAGE_DIR)

    books_data = process_urls_concurrently(urls)  # 处理 URL 列表
    save_to_excel(books_data, EXCEL_FILE)  # 保存数据到 Excel 文件
    logging.info("Done!")  # 完成处理，记录日志


if __name__ == "__main__":
    main()