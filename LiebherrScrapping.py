import datetime
import csv
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import os
import time

#1111111111111111111111111111111111111111111111
# urls = [
#     "https://liebherr.com.ua/category/kholodilniki",
#     "https://liebherr.com.ua/category/kholodilniki?page=2",
#     "https://liebherr.com.ua/category/kholodilniki?page=3",
#     "https://liebherr.com.ua/category/kholodilniki?page=4",
#     "https://liebherr.com.ua/category/kholodilniki?page=5",
#     "https://liebherr.com.ua/category/kholodilniki?page=6",
#     "https://liebherr.com.ua/category/kholodilniki?page=7",
#     "https://liebherr.com.ua/category/kholodilniki?page=8",
#     "https://liebherr.com.ua/category/morozilnye-kamery",
#     "https://liebherr.com.ua/category/morozilnye-kamery?page=2",
#     "https://liebherr.com.ua/category/vinnye-i-sigarnye-shkafy",
#     "https://liebherr.com.ua/category/vinnye-i-sigarnye-shkafy?page=2",
# ]
#
# count = 0
# for url in urls:
#     count += 1
#     try:
#         driver = webdriver.Chrome(
#             executable_path=r'C:\Python\LiebherrSrapping\chrome_driver\chromedriver'
#         )
#         driver.get(url=url)
#         time.sleep(5)
#         with open(f'html/index{count}.html', 'w', encoding="utf-8") as file:
#             file.write(driver.page_source)
#         time.sleep(5)
#     except Exception as _ex:
#         print(_ex)
#     finally:
#         driver.close()
#         driver.quit()
#11111111111111111111111111111111111111111111

#22222222222222222222222222222222222222222222
# dir_name = 'C:\Python\LiebherrSrapping\html'
# list = os.listdir(dir_name)
#
# list_tov_href = []
# for item in list:
#     with open(f'C:\Python\LiebherrSrapping\html\{item}', encoding='utf-8') as file:
#         src = file.read()
#
#     soup = BeautifulSoup(src, 'lxml')
#     all_prod_href = soup.find_all('a', class_='product-card__name d-block position-relative text-decoration-none product-none-opacity')
#     for item in all_prod_href:
#         item_href = item.get('href')
#         list_tov_href.append(item_href)
# print(list_tov_href)
# print(len(list_tov_href))
#
# count = 0
# for url in list_tov_href:
#     count += 1
#     try:
#         driver = webdriver.Chrome(
#             executable_path=r'C:\Python\LiebherrSrapping\chrome_driver\chromedriver'
#         )
#         driver.get(url=url)
#         time.sleep(5)
#         with open(f'tov_html/index{count}.html', 'w', encoding="utf-8") as file:
#             file.write(driver.page_source)
#         time.sleep(1)
#     except Exception as _ex:
#         print(_ex)
#     finally:
#         driver.close()
#         driver.quit()
#     print(count)
#
#2222222222222222222222222222222222222222222

#3333333333333333333333333333333333333333333
starttime = datetime.datetime.now().strftime('%d_%m_%Y_%H_%M')
dir_name = r'C:\Python\LiebherrSrapping\tov_html'
list = os.listdir(dir_name)
datetime.datetime.now()
with open(f"liebherr_{starttime}.csv", "w", newline='', encoding="cp1251") as file:
    writer = csv.writer(file)
    writer.writerow(
        (
            "name",
            "sku",
            "price",
        )
    )
for item in list:
    with open(fr'C:\Python\LiebherrSrapping\tov_html\{item}', encoding="utf-8") as file:
        src = file.read()

    try:
        soup = BeautifulSoup(src, "lxml")
        name = soup.find('h1', class_='product-name mb-0').text.strip()
        sku = soup.find('div', class_='product-text').find('span').text.strip()
        price = soup.find('div', class_='product-cost new-price d-flex align-items-baseline mr-4 pr-2').find('span').text.strip()
        # image_href = 'https://shop.miele.ua' + soup.find(class_='product-img').get('href')
        # out_of_stock = soup.find(class_='product-status').find('span').text
        # date = soup.find(class_='date-availability').find('span').text
    except AttributeError:
        print(f'Error {name}')

    with open(f"liebherr_{starttime}.csv", "a", newline='', encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(
            (
                name,
                sku,
                price,
            )
        )
