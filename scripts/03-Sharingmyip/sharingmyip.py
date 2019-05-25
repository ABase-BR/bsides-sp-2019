import requests
from bs4 import BeautifulSoup

def green_sharingmyip(url,ip):
    rec_site = requests.get('http://sharingmyip.com/?site='+url)

    soup = BeautifulSoup(rec_site.text,'html.parser')

    qt_textarea = len(soup('textarea'))
    msg_list = ['Site (s) neste endereço','DNS para ','Entradas de DNS relacionadas para']
    #for msg in range(msg_list):
    for i in range(qt_textarea):
        if (i == 0):
            print(msg_list[0]+" "+ip)
            print(soup('textarea')[i].string)
        elif i == 1:
            print(msg_list[1]+" "+url)
            print(soup('textarea')[i].string)
        elif i == 2:
            print(msg_list[2]+" "+url)
            print(soup('textarea')[i].string)
        else:
            print("Aconteceu algo errado :D")

ip = "8.8.8.8"
url = "businesscorp.com.br"
print(green_sharingmyip(url,ip))
