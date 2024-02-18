from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

import pandas as pd
import time
import os

web = 'https://nlab.itmedia.co.jp/research/category/entertainment/anime'

chrome_path = './chromedriver.exe'

options = Options()
options.add_argument('--no-sandbox')
options.add_argument('--disable-gpu')
options.add_argument('--disable-application-cache')
options.add_argument('--disable-extensions')

service = Service(chrome_path)

driver = webdriver.Chrome(service=service, options=options)

output_file = 'itmedia_animate_paginations.csv'
output_folder = 'output'
output_url = f'{os.getcwd()}/{output_file}'

driver.get(web)
driver.maximize_window()
# Pagination
pagination = driver.find_element(By.XPATH, '//div[@class="wp-pagenavi"]')
pages = pagination.find_elements(By.TAG_NAME, 'a')
last_page = int(pages[-3].text)
current_page = 1
article_title = []
article_time = []
article_author = []
article_detail_link = []
article_image_thumb = []
print(f"開始爬取資料～總頁數{last_page}頁")
while current_page <= last_page:
    print(f"開始爬取第{current_page}頁")
    time.sleep(5)
    container = driver.find_element(By.CLASS_NAME, 'mainBoxList')
    articles = container.find_elements(By.XPATH, '//article')

    path_for_title = '//div[contains(@class,"article-contents")]/div[contains(@class,"article-title")]/h3/a'
    path_for_art_time = '//div[contains(@class,"article-contents")]/div[contains(@class,"article-meta")]/time'
    path_for_author = '//div[contains(@class,"article-contents")]//div[contains(@class,"article-author")]/a'
    path_for_thumb = '//a[contains(@class,"article-thumb")]/div[contains(@class,"myBoxBG")]/img'
    path_for_link = '//div[contains(@class,"article-contents")]/div[contains(@class,"myBoxBtn")]/a'

    for article in articles:
        title = article.find_element(By.XPATH, path_for_title).text
        art_time = article.find_element(By.XPATH, path_for_art_time).get_attribute("datetime")
        author = article.find_element(By.XPATH, path_for_author).text
        thumb = article.find_element(By.XPATH, path_for_thumb).get_attribute("src")
        link = article.find_element(By.XPATH, path_for_link).get_attribute("href")
        article_title.append(title)
        article_time.append(art_time)
        article_author.append(author)
        article_image_thumb.append(thumb)
        article_detail_link.append(link)
        current_page = current_page + 1

        try:
            next_page = driver.find_element(By.XPATH, '//a[contains(@class,"nextpostslink")]')
            next_page.click()

        except:
            print("已無頁可爬")

            print("結束爬取資料～")
            driver.quit()
            print(f"開始資料存擋～檔名{output_file}")
            data_dict = {'article_title': article_title, 'article_time': article_time, 'article_author': article_author,
                         'article_image_thumb': article_image_thumb, 'article_detail_link': article_detail_link}

            df_anime = pd.DataFrame(data_dict)
            if not os.path.exists(output_folder):
                print(f"{output_folder} 資料夾不存在～建立資料夾")
                os.mkdir(output_folder)
            df_anime.to_csv(output_url, index=False)
            print(f"資料存擋完畢～{output_url}")
