import json
import requests

def archive_search(url):
    archive = "http://archive.org/wayback/available"
    try:
        r = requests.post(archive, data={'url': url})
    except Exception as e:
        print("Ocorreu um erro: %s" % (e))
    return r.text

def green_archive(url):
    resposta_archive = json.loads(archive_search(url))
    return resposta_archive['results']


url="facebook.com"
print(green_archive(url))