# Infoga
Com o Infoga podemos coletar informações , como por exemplo
- Contas de email
- IP
- Nome de host
- Pais

Ele usa diversas fontes publicas
- Mecanismos de busca
- Servidores de chave PGP
- Shodan

Além de checar se o email foi vazado usando a API do **havebeenpwned.com**.


## Link do projeto
```sh
https://github.com/m4ll0k/Infoga
```

## Instalando Infoga
Depois de baixar o projeto e entrar no diretório podemos instalar o projeto.
```sh
python setup.py install
```

Instalando libs
```sh
pip install chardet
pip install certifi
pip install idna
```

## Como usar
```sh
python infoga.py --domain "businesscorp.com.br" -v 3
```


## Usando o Docker
Antes de começar precisamos ter o Docker instalado , com ele já instalado vamos criar um arquivo **Dockerfile**.
```sh
FROM python:3
RUN apt-get update
WORKDIR /root
RUN git clone https://github.com/m4ll0k/Infoga
WORKDIR Infoga
RUN pip install colorama
RUN pip install requests
RUN pip install urllib3
RUN pip install chardet
RUN pip install certifi
RUN pip install idna
ENTRYPOINT ["python","/root/Infoga/infoga.py"]
```

Depois de criar o arquivo vamos realizar build da imagem
```sh
sudo docker build -t "greenmind/infoga:1" .
```

Depois da imagem criada podemos usar ela da seguinte forma
```sh
sudo docker run -it --rm "greenmind/infoga:1" --domain businesscorp.com.br
```