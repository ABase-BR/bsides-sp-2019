# pwnedOrNot
O pwnedOrNot é uma ferramenta que usa informações OSINT para encontrar senha e endereços de email comprometidos.


## Link do projeto
Podemos encontrar o projeto no github.
```sh
https://github.com/thewhiteh4t/pwnedOrNot
```

### Criando container usando Docker
Podemos criar um container da seguinte forma.

Com o Docker já instalado vamos baixar o projeto e entrar no diretório.
```sh
git clone https://github.com/thewhiteh4t/pwnedOrNot
```

Depois vamos realizar um build para criar a imagem.
```sh
sudo docker build -t "greenmind/pwnedornot:1" bash
```

Podemos agora usar a nossa imagem
```sh
sudo docker run -it --rm "greenmind/pwnedornot:1" -e "juulinholive@gmail.com"
sudo docker run -it --rm "greenmind/pwnedornot:1" -c "xvideos.com"
```