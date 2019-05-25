import pprint
from dnsdumpster.DNSDumpsterAPI import DNSDumpsterAPI
#pip install dnsdumpster --user

pp = pprint.PrettyPrinter(indent=4)
results = DNSDumpsterAPI().search('microsoft.com')
pp.pprint(results)
