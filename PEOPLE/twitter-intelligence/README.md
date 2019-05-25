# twitter-intelligence

O projeto twitter-intelligence nos ajuda no rastreamento e analise do Twitter.
```sh
https://github.com/batuhaniskr/twitter-intelligence
```


O Twiter-intelligence é uma ferramenta que tem como meta buscar por informações publicas de twitters.


## Usando o Docker
Vamos criar uma imagem para usar , mas precisamos ter o Docker instalado.


Gerando uma nova imagem
```sh
sudo docker build -t "greenmind/twitter-intelligence:1" .
```

Como usar ?
```sh
sudo docker run -it --rm "greenmind/twitter-intelligence:1"
```

Depois de entrar no container podemos executar os comandos.

Podemos ver um exemplo para buscar por **leak** usando o **--query**.
```sh
python3 tracking.py --query "leak" --since 2015-09-10 --until 2019-01-01 --maxtweets 10
```

Podemos buscar informações de um determinado twitter , nesse exemplo eu estou usando o meu proprio **greenmind_br**.
```sh
python3 tracking.py --username "greenmind_br" --since 2015-09-10 --until 2019-01-01 --maxtweets 10
```

> Se o twitter ter uma conta privada pode ser um problema buscar por informações