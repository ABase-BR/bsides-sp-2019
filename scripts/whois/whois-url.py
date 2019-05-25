import requests
from pprint import pprint

r = requests.get('https://api.hackertarget.com/whois/?q=businesscorp.com.br')

print(r.status_code)
print(r.text)
print(r.headers['content-type'])
pprint(r.text)
