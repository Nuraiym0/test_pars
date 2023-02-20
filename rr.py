# import csv
# import requests
# from bs4 import BeautifulSoup as BS

# url ='https://www.mashina.kg/search/all/'
# def write_to_csv(data):
#     import csv
#     with open('mashina_kg.csv', 'a') as f:
#         writer = csv.writer(f, delimiter=' ')
#         writer.writerow((data['title'], data['price'], data['info'], data['image']))

# def get_product_data(product_box:BS) -> dict:
#     title = product_box.find('div',{'class':'title'}).text.replace('\n', '').strip()

#     price = ' '.join(product_box.find('div', {'class':'price'}).find('p').text.replace('\n', '').split())
#     # lol1 = ''.join(product_box.find('div', {'class': 'info-wrapper'}).find('p',{'class':'year-miles'}).text.replace('\n', '').strip())
#     # lol3 = ''.join(product_box.find('div', {'class': 'info-wrapper'}).find('p',{'class':'body-type'}).text.replace('\n', '').strip())
#     # lol4 = ''.join(product_box.find('div', {'class': 'info-wrapper'}).find('p',{'class':'volume'}).text.replace('\n', '').strip())
#     # lol2 = product_box.find('div', {'class':'info-wrapper'}).find('p').find('i')['title']
    
#     info = str()
#     # info += (' ' +lol1)
#     # info += (',' +lol3)
#     # info += (',' +lol4)
#     # info += (', цвет: ' + lol2)
#     try:
#         image = product_box.find('a').find('img').get('data-src')
#     except:
#         image = 'No image'
#     data = {"title": title, "price": price, 'info': info, 'image': image}
#     write_to_csv(data)
#     return data

# def get_total_pages (soup):
#     pages_ul = soup.find('div', class_="search-results-table").find('ul', class_='pagination')
#     last_page = pages_ul.find_all('li')[-1]
#     total_pages = last_page.find('a').get('href').split('=')[-1]
#     return int(total_pages)

# def get_data_by_category(category: str) -> dict:
#     soup = get_soup(url + category)
#     last_page = get_total_pages(soup)
#     all_products = []
#     for page in range(1, last_page+1):
#         print(f'{url}{category}?page={page}')
#         soup = get_soup(f'{url}{category}?page={page}')
#         products = get_all_products(soup)
#         all_products.extend(products)
#     return {category: all_products}

# def get_all_products(soup:BS):
#     products = []
#     for product_box in soup.find_all('div',{'class':'list-item'}):
#         product_data = get_product_data(product_box)
#         products.append(product_data)
#     return products

# def get_soup(url:str) -> BS:
#     headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36'}
#     import time
#     time.sleep(5)
#     response = requests.get(url,headers=headers)
#     html = response.text
#     soup = BS(html, 'lxml')
#     return soup

# def main():
#     soup = get_soup('https://www.mashina.kg/search/all/')
#     categories = url
#     products = get_all_products(soup)
#     all_data = {}
#     for category in categories:
#         data = get_data_by_category(category)
#         all_data.update(data)

# main()





