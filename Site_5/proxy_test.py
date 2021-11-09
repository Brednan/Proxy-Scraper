import requests

proxy={
    "http":"http://64.124.38.142:8080",
    "https":"https://64.124.38.142:8080"
}


r = requests.get('https://api.mojang.com/users/profiles/minecraft/xJorn', proxies=proxy)

try:
    print(r.status_code)
except:
    print(r.status_code)