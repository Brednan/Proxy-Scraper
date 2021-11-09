import site_1_mechanisms as s1
import site_3_mechanisms as s3
import site_4_mechanisms as s4

def site_1_list(headless, geckodriver):
    driver = s1.initialize(headless, geckodriver)
    ip_list = s1.get_ip_list(driver)
    driver.quit()
    return ip_list


def site_3_list(headless, geckodriver):
    driver = s3.initialize(headless, geckodriver)
    ip_list = s3.get_list(driver)
    driver.quit()
    return ip_list


def site_4_list(headless, geckodriver):
    driver = s4.initialize(headless, geckodriver)
    ip_list = s4.scrape_list(driver)
    driver.quit()
    return ip_list


def save_to_file(directory, proxies):
    f = open(directory, 'w')
    for i in proxies:
        f.write(f'{i}\n')
    f.close()

