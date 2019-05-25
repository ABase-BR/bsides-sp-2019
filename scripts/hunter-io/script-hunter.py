from pyhunter import PyHunter
import pprint

# https://github.com/VonStruddle/PyHunter
# pip install pyhunter


hunter = PyHunter('SUA-KEY')
hunter.domain_search('businesscorp.com.br')

pp = pprint.PrettyPrinter(indent=4)
pp.pprint(hunter.domain_search('businesscorp.com.br'))
