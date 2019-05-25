# Vazamentos
Vazamento de dados pode ser um problema para as empresas , funcionários e clientes.

Sabendo isso vou compartilhar alguns projetos que auxiliam na busca de vazamentos.

## dehashed
O dehashed nos ajuda com a busca de possíveis vazamentos , precisamos passar qual domínio queremos testar
```sh
https://dehashed.com/search?query=%22businesscorp.com.br%22
```

## intelx.io
intelx.io também nos ajuda a buscar informações , ele nos retorna possíveis pastes com possíveis informações.

Ele busca por informações em Pastebins e na internet.
```sh
https://intelx.io/?s=aplicativos.org
```

## psbdmp
Podemos buscar por informações de duas formas com o **psbdmp** , a primeira é usando a API.

Essa API nos retorna informações do tipo
- ID
- TAG
- data

OS IDs são os IDS do pastebin e facilita na hora de analisar.

```sh
https://psbdmp.ws/api/search/businesscorp.com.br
```

Ou podemos usar o site
```sh
https://psbdmp.ws
```



## grayhatwarfare
Com o grayhatwarfare podemos buscar por possiveis arquivos.

```sh
https://buckets.grayhatwarfare.com/results/facebook.com
```