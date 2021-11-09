import bot_functions as bf


all_proxies = []


for i in bf.site_1_list(True):
    all_proxies.append(f'{i["address"]}:{i["port"]}')


for i in bf.site_3_list(True):
    all_proxies.append(f'{i["address"]}:{i["port"]}')


for i in bf.site_4_list(True):
    all_proxies.append(f'{i["address"]}:{i["port"]}')

bf.save_to_file(r'D:\Desktop\Python Desktop Apps\Proxy Scraper\output.txt', all_proxies)