#Shodan
from shodan import Shodan

def green_shodansearch(name_host,shodan_key):
    # ADD Key config
    api = Shodan(shodan_key)
    host = api.host(name_host)
    # print(ipinfo)
    # Print general info
    print("""
IP: {}
Organization: {}
Operating System: {}
                    """.format(host['ip_str'], host.get('org', 'n/a'), host.get('os', 'n/a')))
    # Print all banners
    for item in host['data']:
        print("""
Port: {}
                            """.format(item['port']))

nome_host = "37.59.174.225"
shodan_key = "SUA-KEY"
print(green_shodansearch(nome_host,shodan_key))
