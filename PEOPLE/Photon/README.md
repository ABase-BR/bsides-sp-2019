# Photon
```sh
https://github.com/s0md3v/Photon/
```

Photon é um projeto que nos auxiliar na busca de informações de um determinado site e podemos extrair informações como por exemplo
- URLS
- Parâmetros de URL
- Intel(Email,contas de redes sociais,amazon buckets)
- Arquivos (PDF,PNG,XML)
- Chaves secretas(API keys e hashs)
- Subdomínios
- Relações de DNS


## Docker
Com o Docker instalado é só ir para o diretório do projeto para realizar o build da imagem.

```sh
sudo docker build -t "greenmind/photon:1" .
```

Depois da imagem criada podemos usar ela da seguinte forma
```sh
sudo docker run -it --rm -v"${PWD}:/Photon" "greenmind/photon:1" -u businesscorp.com.br
```

> Vamos usar o **-v"${PWD}:/Photon"** para ele salvar no mesmo diretório a saída.