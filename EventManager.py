import bot_functions as bf
import Site_5.bot_functions as bf5
import os

def onSubmission(headless_opt, file_dir, popup, geckodriver):
    if len(file_dir.strip()) > 0:
        proxies = []
        
        for i in bf.site_1_list(headless_opt, geckodriver):
            proxies.append(f'{i["address"]}:{i["port"]}')

        for i in bf.site_3_list(headless_opt, geckodriver):
            proxies.append(f'{i["address"]}:{i["port"]}')
        
        for i in bf.site_4_list(headless_opt, geckodriver):
            proxies.append(f'{i["address"]}:{i["port"]}')

        for i in bf5.site_5_list(headless_opt, 'http://free-proxy.cz/en/proxylist/country/all/https/ping/level1', geckodriver):
            proxies.append(f'{i["address"]}:{i["port"]}')

        for i in bf5.site_5_list(headless_opt, 'http://free-proxy.cz/en/proxylist/country/all/https/ping/level1/2', geckodriver):
            proxies.append(f'{i["address"]}:{i["port"]}')

        bf.save_to_file(file_dir, proxies)
        popup('Finished!', '200x40')

    else:
        popup('Invalid Submission!', '250x70')
