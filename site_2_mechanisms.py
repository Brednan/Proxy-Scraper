from selenium import webdriver

#-----This Site Does Not Work!-----

def initialize(page):
    web_driver = webdriver.Firefox(executable_path=r'D:\Desktop\Python Desktop Apps\Proxy Scraper\geckodriver.exe')
    web_driver.get(f'https://www.freeproxylists.net/?page={page}')
    return web_driver


def get_list(driver):
    proxy_list = driver.find_elements_by_xpath('/html/body/div[1]/div[2]/table/tbody/tr')
    _list = []

    for i in proxy_list:
        try:
            address = i.find_element_by_xpath('./td[1]/a')
            port = i.find_element_by_xpath('./td[2]')
            if(address.text != 'IP Address'):
                _list.append({
                    'address':address.text,
                    'port': port.text
                })
        except:
            pass

    return _list