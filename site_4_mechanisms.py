from selenium import webdriver
from selenium.webdriver.firefox.options import Options


def initialize(headless, geckodriver):
    options = Options()
    options.headless = headless
    web_driver = webdriver.Firefox(options=options, executable_path=geckodriver)
    web_driver.get('https://spys.one/en/https-ssl-proxy/')
    return web_driver


def scrape_list(driver):
    _list=[]
    
    try:
        columns = driver.find_elements_by_xpath('/html/body/table[2]/tbody/tr[4]/td/table/tbody/tr')
        print('Successfully found proxy list in site 4!')
        for c in columns:
            try:
                address = c.find_element_by_xpath('./td[1]/font')
                address_split = address.text.split(':')
                if address_split[0] != 'Proxy address':
                    _list.append({
                        'address':address_split[0],
                        'port':address_split[1]
                    })
            except:
                pass
    except:
        print('Error on site 4!')
    return _list
    