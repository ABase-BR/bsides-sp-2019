# Sherlock
O Sherlock é um projeto que nos auxilia na busca por nomes de usuários nas redes sociais.

```sh
https://github.com/sherlock-project/sherlock
```

## Docker
Podemos usar o Docker para nos auxiliar no uso da imagem , só precisamos do Docker instalado e o **sherlock** já tem suporte.

Para criar a imagem , precisamos fazer o seguinte comando.
```sh
sudo docker build -t "greenmind/sherlock:1" .
```

Podemos usar o **sherlock** da seguinte forma
```sh
sudo docker run -it --rm "greenmind/sherlock:1" greenmind-sec
```