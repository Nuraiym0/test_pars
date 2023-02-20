import time
from selenium import webdriver #api
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common import by
from selenium.common.exceptions import TimeoutException


service =  Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
URI = 'https://www.kijiji.ca/b-apartments-condos/city-of-toronto/c37l1700273'


def get_source_code()->None:
    driver.get(url=URI)
    

    # while True:
    #     try:
    #         element = WebDriverWait(driver=driver, timeout=2).until(expected_conditions.presence_of_element_located(by.By.CLASS_NAME('clearfix')))
    #         print(element)
    #         with open ('res.txt', 'w' ) as f:
    #             f.write(element.text)
    #         break
    #     except TimeoutException as _ex:
    #         print(_ex)
    #         break
        









def main()->None:
    get_source_code(URI)

    print(get_source_code)


if __name__ == '__main__':
    main()