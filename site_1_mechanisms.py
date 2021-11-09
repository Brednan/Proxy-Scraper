from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options

def initialize(headless, geckodriver):
    options = Options()
    options.headless = headless
    web_driver = webdriver.Firefox(options=options, executable_path=geckodriver)
    web_driver.get('https://free-proxy-list.net/')
    return web_driver


def get_ip_list(driver):
    array = []
    try:
        _list = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.XPATH, '/html/body/section[1]/div/div[2]/div/table/tbody/tr'))
        )
        print('Successfully found proxy list in site 1!')
        for i in _list:
            address = i.find_element_by_xpath('./td[1]')
            port = i.find_element_by_xpath('./td[2]')
            array.append({
                "address": address.text,
                "port": port.text
            })
    except:
        print('Error on site 1!')
        pass

    return array