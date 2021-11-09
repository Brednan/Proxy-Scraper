from . import site_5_mechanisms

def site_5_list(headless_opt, url, geckodriver):
    driver = site_5_mechanisms.initialize(headless_opt, url, geckodriver)
    elements = site_5_mechanisms.iteration(driver)
    driver.quit()
    return elements