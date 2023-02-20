import csv
import requests
from bs4 import BeautifulSoup as bs
from datetime import datetime
# from peewee import *
# import pandas as pd

# main_url = 'https://www.kijiji.ca/b-apartments-condos/city-of-toronto/c37l1700273'


def get_html(url):
    # headers = {'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Mobile Safari/537.36'}
    response = requests.get(url,) #headers=headers)
    return response.text
    # print(response.status_code)
    # print(response.text)

def get_total_pages(html):
    soup = bs(html, 'lxml')
    # print(soup.prettify())
    pages = soup.find('div', class_='pagination')
    # print(pages)
    last_page = pages.find_all('a')[-3].get('href').split('/')[-2].split('-')[-1]
    return int(last_page)
    # print(int(last_page))

def write_to_csv(data):
    with open('parsing.csv', 'a') as f:
        writer = csv.writer(f, delimiter='/')
        writer.writerow((data['time'],
                        data['price'],
                        data['image']))


def get_page_data(html):
    soup = bs(html, 'lxml')
    product_list = soup.find('div', class_="layout-3 new-real-estate-srp").find('div', class_="col-2 new-real-estate-srp")#.find('div',class_="clearfix").find('div', class_='info').find('div', class_='price') #class="price"
    # print(product_list)
    products = product_list.find_all('div', class_="clearfix")#.find('div', class_='info')
    # print(products)


    for product in products:

        time = product.find('div', class_='info').find('div', class_="location").find('span', class_='date-posted').text.replace('\n', '').strip()
        # print(time)
        price = product.find('div', class_='info').find('div', class_="price").text.replace('\n', '').strip()
        # print(price)
            
        try:
            image = product.find('div', class_='left-col').find('div', class_="image").find('img').get('data-src')
            # print(image)
        except:
            image = ''

        data = {"time": time, "price": price,'image': image}
        # print(data)
        write_to_csv(data)
        

def main():
    main_url = 'https://www.kijiji.ca/b-apartments-condos/city-of-toronto/c37l1700273'
    pages = '?page-'

    total_pages =get_total_pages(get_html(main_url))
    # print(total_pages)
    for page in range(1, total_pages+1): #10
        url_with_page = main_url + pages + str(page)
        # print(url_with_page)
        html = get_html(url_with_page)
        data=get_page_data(html)
        print (f'page{data}')



main()









