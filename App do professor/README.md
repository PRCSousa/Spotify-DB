# Desenvolvimento da aplicação da 2ª parte do projeto


## Programação

A estrutura deverá ser similar à da aplicação [MovieStreamApp](https://moodle.up.pt/mod/resource/view.php?id=77946) que vimos nas aulas teóricas:

- Deve editar o código Python da aplicação em `app.py`. 
- Deve colocar as templates de geração de HTML na pasta `templates`. 


## Referências

- [Aplicações BD com SQL embebido](https://moodle.up.pt/mod/resource/view.php?id=77931) (slides das teóricas)
- [MovieStream - aplicação exemplo](https://moodle.up.pt/mod/resource/view.php?id=77946)
- [Linguagem HTML](https://developer.mozilla.org/en-US/docs/Web/HTML)
- [PyMySQL](https://pymysql.readthedocs.io/en/latest/index.html)
- [Flask](https://flask.palletsprojects.com/en/1.1.x/)
- [Jinja templates](https://jinja.palletsprojects.com/en/2.10.x/templates/)


## Instalação de software

Precisa de ter o Python 3 e o gestor de pacotes pip instalado.
Experimente executar `python3 --version` e `pip3 --version` para saber
se já estão instalados. Em caso negativo, pode por exemplo em Ubuntu
executar:

```
sudo apt-get install python3 python3-pip
```

Tendo Python 3 e pip instalados, deve instalar as bibliotecas Python `Flask`, `PyMySQL`, e `cryptography` em Python, executando o comando:

```
pip3 install --user Flask==1.1.4 PyMySQL==1.0.2 cryptography==36.0.0
``` 

## Configuração de acesso à BD

Edite o ficheiro `db.py` no que se refere à configuração da sua BD, modificando os parâmetros `DB` (nome da base de dados), `USER` (nome do utilizador) e `PASSWORD` (senha do utilizador).

Em __computadores dos laboratório do DCC__ esses valores costumam ser `guest` para `USER` e `DB`, e `aDammGoodP@ssw0rd` para `PASSWORD`. Pode confirmar se os valores são esses em um PC do laboratório do DCC inspecionando o conteúdo do ficheiro `/etc/my.cnf` (ex. com o comando `cat /etc/my.cnf`).

```
$ cat /etc/my.cnf
...
[client]
user=guest
password=aDammGoodP@ssw0rd
...
```

Configurados os parâmetros,  teste o acesso executando:

```
python3 test_db_connection.py NOME_DE_UMA_TABELA
```

Se a configuração do acesso à BD estiver correcto, deverá ser listado o conteúdo da tabela `NOME_DE_UMA_TABELA`, por ex. se a BD configurada for a MovieStream:

```
$ python3 test_db_connection.py REGION
SELECT * FROM REGION
5 results ...
{'RegionId': 6, 'Name': 'Other countries', 'RegionManager': 17}
{'RegionId': 7, 'Name': 'America', 'RegionManager': 16}
{'RegionId': 8, 'Name': 'Asia', 'RegionManager': 15}
{'RegionId': 9, 'Name': 'Europe', 'RegionManager': 17}
{'RegionId': 10, 'Name': 'Africa', 'RegionManager': 15}
```

## Execução do servidor da aplicação

Teste agora o servidor executando `python3 server.py`, ex.:

```
$ python3 server.py
2021-05-18 21:40:46 - INFO - Connected to database guest
 * Serving Flask app "app" (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: off
2021-12-08 21:40:46 - INFO -  * Running on http://0.0.0.0:9000/ (Press CTRL+C to quit)
...
```

De seguida abra no seu browser __http://127.0.0.1:9000__ ou __http://localhost:9000__. Deverá ver uma página com uma mensagem __Hello World!__.





