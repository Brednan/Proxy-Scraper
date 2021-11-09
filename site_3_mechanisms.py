from selenium import webdriver
from selenium.webdriver.firefox.options import Options

def initialize(headless, geckodriver):
    options = Options()
    options.headless = headless
    web_driver = webdriver.Firefox(options=options, executable_path=geckodriver)
    web_driver.get('https://www.proxynova.com/proxy-server-list')
    return web_driver


def get_list(driver):
    _list = []
    try:
        proxy_list = driver.find_elements_by_xpath('//*[@id="tbl_proxy_list"]/tbody[1]/tr')
        print('Successfully found proxy list in site 3!')
        for i in proxy_list:
            try:
                address = i.find_element_by_xpath('./td[1]/abbr')
                port = i.find_element_by_xpath('./td[2]')
                _list.append({
                    "address":address.text, 
                    "port": port.text
                })
            except:
                pass
    except:
        print('Error on site 3!')
    return _list