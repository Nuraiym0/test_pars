# import requests
# from bs4 import BeautifulSoup as BS
# import dateparser

# r = requests.get('https://www.kijiji.ca/b-apartments-condos/city-of-toronto/c37l1700273')
# html = BS(r.content, 'html.parser')
# # soup = BS(r.text, 'lxml')

# for el in html.select('.MainContainer > .mainPageContent > .data-listing-id'): #> .location > .date-posted'):
#     time = el.select('.location > .date-posted')
#     print(time[0].text)




















# # def get_item_datetime(item_page,datetime_rule,datetime1_rule):
# #     if item_page is None:
# #         return
# #     soup = BS(item_page, 'lxml')
# #     item_datetime = soup.find(datetime_rule[0],{datetime_rule[1]:datetime_rule[2]})
# #     if item_datetime is not None:
# #         item_datetime = soup.find(datetime_rule[0],{datetime_rule[1]:datetime_rule[2]}).text
# #         item_datetime = dateparser.parse(item_datetime, date_formats=['%d %B %Y %H'])
# #     else:
# #         if (len(datetime1_rule) == 3):
# #             item_datetime = soup.find(datetime1_rule[0],{datetime1_rule[1]:datetime1_rule[2]}).text
# #             item_datetime = dateparser.parse(item_datetime, date_formats=['%d %B %Y %H'])
# #         else:
# #             item_datetime = ''
# #     return item_datetime


# # def get():
# #     item_datetime = soup.select_one('distance > span').text
# #     dt = dateparser(item_datetime, date_formats=['%d %B %Y %H'])
# #     return dt
# # data-listing-id

# #  date-posted

