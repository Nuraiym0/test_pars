# import requests
# from bs4 import BeautifulSoup as BS

# main_url = 'https://www.kivano.kg'

# def get_soup(url: str) -> BS:
#     """
#     Принимает ссылку, отправляет запрос.
#     Возвращает обьект BeautifulSoup с этой страницы
#     """
#     headers = {'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36'}
#     import time
#     time.sleep(5)
#     response = requests.get(url, headers=headers)
#     return BS(response.text, 'lxml')

# def get_all_products_from_page(soup: BS) -> list:
#     """
#     Принимает суп страницы, ищет все блоки с данными о продуктах.
#     """
#     products = []
#     for product in soup.find_all('div', {'class':'product_listbox'}):
#         product_info = get_product_info(product)
#         products.append(product_info)
#     return products

# def get_product_info(product: BS) -> dict:
#     """
#     Принимает блок данных о продукте. Находит title, price, image. Возвращает данные ввиде словаря
#     """
#     title = product.find('div', {'class':'listbox_title'}).text.strip()
#     # extract - вырезает элемент из soup
#     # product.find('div', {'class':'listbox_title'}).extract()
#     # desc = product.find('div', {'class':'product_text'}).text
#     image = product.find('div', {'class':'listbox_img'}).find('img').get('src')
#     price = product.find('div', {'class':'listbox_price'}).text.strip()
#     return {'title':title, 'price':price, 'image':create_full_image_url(image)}

# def create_full_image_url(url: str):
#     return main_url + url

# def get_last_page(soup: BS):
#     """
#     Находит номер последней страницы
#     """
#     ul = soup.find('ul', {'class':'pagination'})
#     if ul is None:
#         return 1
#     last = ul.find('li', {'class':'last'})
#     return int(last.text)

# def write_to_db(data):
#     """
#     Принимает данные и запиывает их в файл db.json
#     """
#     import json
#     with open('db.json', 'w', encoding='utf-8') as f:
#         json.dump(data, f, ensure_ascii=False)

# def get_all_categories() -> list:
#     """
#     Находит все категории и возвращает список с ссылками на категории
#     """
#     soup = get_soup(main_url)
#     categories = []
#     menu_items = soup.find_all('div', {'class':'leftmenu-item'})
#     for menu_item in menu_items:
#         a = menu_item.find('div', {'class':'leftmenu-title'}).find('a')
#         categories.append(a.get('href'))
#     return categories

# def get_data_by_category(category: str) -> dict:
#     soup = get_soup(main_url + category)
#     last_page = get_last_page(soup)
#     all_products = {}
#     for page in range(1, 4):
#         print(f'{main_url}{category}?page={page}')
#         soup = get_soup(f'{main_url}{category}?page={page}')
#         # отправляем запрос на новую страницу
#         products = get_all_products_from_page(soup)
#         # получаем список продуктов с этой страницы
#         all_products[page]=products
#         # добавляем в общий список продукты с этой страницы

#     return {category: all_products}

# def main():
#     try:
#         categories = get_all_categories()
#         all_data = {}
#         for category in categories:
#             data = get_data_by_category(category)
#             all_data.update(data)
#     finally:
#         write_to_db(all_data)


# if __name__ == '__main__':
#     # __name__ = '__main__' когда мы запускаем сам файл parsing.py
#     # __name__ = 'parsing' когда мы его импортируем
#     main()




# print('=========================================================================================================')






# # # # id="MainContainer" > mainPageContent > class="layout-3 new-real-estate-srp" > class="col-2 new-real-estate-srp > class="container-results large-images >  data-listing-id="1646012473" > class="info" > class="info-container" >  class="price"  > class="location"


# # # # id="MainContainer" > mainPageContent > class="layout-3 new-real-estate-srp" > class="col-2 new-real-estate-srp > class="container-results large-images >  data-listing-id="1646012473" > class="info" > class="left-col" > class="left-col"



# import requests
# from bs4 import BeautifulSoup as BS

# main_url = 'https://www.kijiji.ca/b-apartments-condos/city-of-toronto/c37l1700273'
 


# def get_soup(url: str) -> BS:
#     """
#     Принимает ссылку, отправляет запрос.
#     Возвращает обьект BeautifulSoup с этой страницы
#     """
#     headers = {'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Mobile Safari/537.36'}
#     import time
#     time.sleep(3)
#     response = requests.get(url=url, headers=headers)
#     return BS(response.text, 'lxml')



# def get_all_products_from_page(soup: BS) -> list:
#     """
#     Принимает суп страницы, ищет все блоки с данными о продуктах.
#     """
#     products = []
#     for product in soup.find_all('div', {'class':'layout-3 new-real-estate-srp'}):
#         product_info = get_product_info(product)
#         products.append(product_info)
#     return products


# def get_product_info(product: BS) -> dict:
#     """
#     Принимает блок данных о продукте. Находит title, price, image. Возвращает данные ввиде словаря
#     """
#     day = product.find('div', {'class':'location'}).find('snap', {'class':'date-posted'}).text.strip()
#     # extract - вырезает элемент из soup
#     # product.find('div', {'class':'listbox_title'}).extract()
#     # desc = product.find('div', {'class':'product_text'}).text
#     image = product.find('div', {'class':'image'}).find('img').get('src')
#     price = product.find('div', {'class':'price'}).text.strip()
#     return {'day':day, 'price':price, 'image':create_full_image_url(image)}


# def create_full_image_url(url: str):
#     return main_url + url


# # def get_product_data(product_box:BS) -> dict:
# #     price = product_box.find('div', {'class':"price"}).text.replace('\n', '').strip()
# #     # title = product_box.find('div',{'class':'title'}).text.replace('\n', '').strip()
# #     raise price











# def main():


#     if __name__ == '__main__':
#         # __name__ = '__main__' когда мы запускаем сам файл parsing.py
#         # __name__ = 'parsing' когда мы его импортируем
        
        
#         main()



# print('===============================================================================================')

# # import requests
# # from bs4 import BeautifulSoup as BS


# # url = 'https://www.kijiji.ca/b-apartments-condos/city-of-toronto/c37l1700273'

# # r = requests.get(url)
# # r.text
# # soup = BS(r.text, 'lxml')


# # # # # r = requests.get(url=url, headers=headers)
# # # with open('14.html', 'w') as f:
# # #     f.write(r.text)
# # # soup = BS(r.text, 'lxml')
# # soup.find('div', class_='clearfix')

# # print(soup)
# # # clearfix