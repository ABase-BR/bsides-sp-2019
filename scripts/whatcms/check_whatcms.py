import requests

CHAVE_WHATCMS = "SUA-KEY"
site="www.fatecourinhos.edu.br"

def green_whatcms(site,CHAVE_WHATCMS):
    api = "https://whatcms.org/APIEndpoint"

    r = requests.post(api, data={'key': CHAVE_WHATCMS, 'url': site})
    if r.status_code == 0:
        status_resposta = "Server Failure"
    elif r.status_code == 100:
        status_resposta = "API Key Not Set"
    elif r.status_code == 101:
        status_resposta = "Invalid API Key"
    elif r.status_code == 110:
        status_resposta = "Url Parameter Not Set"
    elif r.status_code == 111:
        status_resposta = "Invalid Url"
    elif r.status_code == 120:
        status_resposta = "Too Many Requests"
    elif r.status_code == 121:
        status_resposta = "You have exceeded your monthly request quota"
    elif r.status_code == 123:
        status_resposta = "Account disabled per violation of Terms and Conditions"
    elif r.status_code == 200:
        status_resposta = "CMS Found"
        print(r.text)
        print(r.headers)
    elif r.status_code == 201:
        status_resposta = "CMS Not Found"
    elif r.status_code == 202:
        status_resposta = "Requested Url Was Unavailable"
    else:
        status_resposta = "Algo errado!"

print(green_whatcms(site,CHAVE_WHATCMS))