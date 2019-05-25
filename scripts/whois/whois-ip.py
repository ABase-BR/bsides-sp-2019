import requests
from pprint import pprint

r = requests.get('https://api.hackertarget.com/whois/?q=186.192.81.5')

print(r.status_code)
print(r.text)
print(r.headers['content-type'])
pprint(r.text)
