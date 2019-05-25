#green_checkrobots
import requests
# Import argv
import sys

def green_checkrobots(url):
    try:
        resposta = requests.get(url + '/robots.txt')
        if (resposta.status_code == 200):
            return resposta.text
        else:
            var = "[ Robots.txt ] - Não encontrado"
            return var
    except Exception as e:
        print("Ocorreu um erro: %s" % (e))


try:
    alvo = sys.argv[1]
    if alvo == "":
        print("Inserir [ site ]")
    else:
        print(green_checkrobots("http://businesscorp.com.br"))
except Exception as e:
    print("Ocorreu um erro: %s" %(e))
#Independente da Execução ou de erro o finally vai sempre ser executado
finally:
    print("Saindo do:"+sys.argv[0])


'''
def checkPHP():
    if 256 != system('which php'):
        return True
    else:
        return False
'''
