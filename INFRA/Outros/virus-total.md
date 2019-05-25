# VirusTotal
O VirusTotal é uma sub divisão da google , é um serviço gratuito que analisa arquivos e URLS , dessa forma ajudando na identificação de conteúdo malicioso por antivirus e scanners de websites.

```sh
https://www.virustotal.com/
```

## Analisando sites
Podemos usar o VirusTotal para buscar informações de um site , por exemplo em
```sh
https://www.virustotal.com/gui/home/search
```

Podemos passar **domínios** , **IPS** , **URLS** e aquivos.

Vou usar só IPS e domínios.

### Domínios
Podemos analisar domínios usando a URL seguida do site **https://www.virustotal.com/gui/domain/** que no caso é o Lab **aplicativos.org**.
```sh
https://www.virustotal.com/gui/domain/aplicativos.org/
```

Vamos ter um feedback sobre o que a comunidade acha do site , além de informações como
- Onde foi registrado
- Quando foi criado
- Ultima atualização

Além disso temos opções como
- Detalhes
- Relações
- Comunidade

#### Detalhes
Já tem detalhes temos as seguinte informações
- Categorias
- Whois

```sh
https://www.virustotal.com/gui/domain/aplicativos.org/details
```

#### Relações
- Resoluções de DNS
- Subdominios

### IPS
Temos as opções
- Relações
- Comunidade

Podemos tambem realizar testes em IPS , na pagina a seguir é possivel ver um feedback da comunidade
```sh
https://www.virustotal.com/gui/ip-address/0.0.0.0/
```

#### Relações
Temos informações de subdomínios
```sh
https://www.virustotal.com/gui/ip-address/0.0.0.0/relations
```

#### Comunidade
Podemos encontrar feedback da comunidade.
```sh
https://www.virustotal.com/gui/ip-address/0.0.0.0/community
```