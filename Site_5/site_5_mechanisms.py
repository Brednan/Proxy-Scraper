from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def initialize(headless_opt, url, geckodriver):
    options = Options()
    options.headless = headless_opt
    driver = webdriver.Firefox(options=options, executable_path=geckodriver)
    driver.get(url)
    return driver


def iteration(driver):
    proxies = []
    try:
        elements = WebDriverWait(driver, 5).until(
            EC.presence_of_all_elements_located((By.XPATH, '//*[@id="proxy_list"]/tbody/tr'))
        )
        print('Successfully found proxy list in site 5!')
        for e in elements:
            try:
                address = e.find_element_by_xpath('./td[1]')
                port = e.find_element_by_xpath('./td[2]/span')
                if len(address.text) > 0:
                    proxies.append({
                        'address': address.text,
                        'port':port.text
                    })
            except:
                pass
    except:
        print('Error on site 5!')
        pass

    return proxies
