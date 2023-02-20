# from selenium_stealth import stealth




# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options

# chrome_options = Options()
# chrome_options.add_argument('--no-sandbox')
# chrome_options.add_argument('--headless')
# chrome_options.add_argument('--disable-gpu')
# chrome_options.add_argument('--disable-dev-shm-usage')
# chrome_options.add_argument('--profile-directory=Default')
# chrome_options.add_argument('--user-data-dir=~/.config/google-chrome')
# # driver = webdriver.Chrome(options=options)




# driver = webdriver.Chrome(options=chrome_options)
# url = 'https://www.kijiji.ca/b-apartments-condos/city-of-toronto/c37l1700273'
# driver.get(url) 
# get_url = driver.current_url 
# print(get_url)

# stealth(driver,
#         languages=["en-US", "en"],
#         vendor="Google Inc.",
#         platform="Win32",
#         webgl_vendor="Intel Inc.",
#         renderer="Intel Iris OpenGL Engine",
#         fix_hairline=True,
#         )




# for page in range(1-100):
#     url = f'https://www.kijiji.ca/b-apartments-condos/city-of-toronto/page-{page}/c37l1700273?ad=offering'

#     driver.get(url)

#     blocks = driver 