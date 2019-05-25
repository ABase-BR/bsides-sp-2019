#pip install pywhatcms
from pywhatcms import whatcms

whatcms('SUA-KEY', 'fatecourinhos.edu.br')

print(whatcms.name)
print(whatcms.code)


print(whatcms.confidence)
print(whatcms.cms_url)
print(whatcms.version)
print(whatcms.msg)
print(whatcms.id)
print(whatcms.request)
print(whatcms.request_web)
