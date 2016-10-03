# Lançamento de Horas
> Simples sistema para lançamento de horas via terminal/cron

O objetivo desse projeto é automatizar tarefas como lançar os horários de entrada e saída ou gerar o total de horas mensal.

### Configuração

Uma vez feito o clone do projeto é necessário criar um arquivo de configuração chamado **perfil.conf** dentro da pasta **conf** com o seguinte:
```
usuario = "<nome_usuario>"
senha = "<senha>"
projeto = "<projeto>"
subProjeto = "<sub_projeto>"
tipoAtividade = "<tipo_atividade>"
```

Esses dados serão usados por "default" dentro da aplicação. Existem modos de sobrescreve-los, porém para garantir
um funcionamento estável é inteligente deixar esses campos já configurados.


### Funções (algumas em desenvolvimento)

A aplicação no terminal gira em torno do arquivo **console.py**.


```shell
~$ python3 console.py -h
usage: console.py [-h] {lancar,projetos,dimed,sub-projetos,atividades} ...

Cliente para lançamento de horas

positional arguments:
  {lancar,projetos,dimed,sub-projetos,atividades}
                        Lança horas no sistema | Lista projetos, sub-projetos
                        e atividades

optional arguments:
  -h, --help            show this help message and exit
```

As opções portanto são:
- lancar
- projetos
- dimed
- sub-projetos
- atividades

### Lançar

Commando para lançamento de hora.
```shell
~$ python3 console.py lancar -h
usage: console.py lancar [-h] [-s START] [-f FINISH] [-d DATE] [-u USER]
                         [-p PASSWORD] [-D DESCRIPTION] [-P PROJECT]
                         [-S SUBPROJECT] [-T TYPE] [-y YES]

optional arguments:
  -h, --help            show this help message and exit
  -s START, --start START
                        start hour with format hh/mm
  -f FINISH, --finish FINISH
                        finish hour with format hh/mm
  -d DATE, --date DATE  reference date
  -u USER, --user USER  user name
  -p PASSWORD, --password PASSWORD
                        password
  -D DESCRIPTION, --description DESCRIPTION
                        task description
  -P PROJECT, --project PROJECT
                        project id
  -S SUBPROJECT, --subProject SUBPROJECT
                        sub-project id
  -T TYPE, --type TYPE  activity type id
  -y YES, --yes YES     not ask for continue
```

* Lembrando que se você criou o arquivo **perfil.conf** muitos desses dados já serão adicionados sem a necessidade de você seta-los.

### Dimed

Comando para gerar uma tabela do total de horas dia-a-dia do mês. (necessário para lançar no tracegp da Dimed)

```shell
~$ python3 console.py dimed -h 
usage: console.py dimed [-h] [-u USER] [-p PASSWORD]

optional arguments:
  -h, --help            show this help message and exit
  -u USER, --user USER  user name
  -p PASSWORD, --password PASSWORD
                        password
```

### Demais comandos

- projetos
- atividades
- sub-projetos

Todos servem para listar as opções que o seu perfil tem e assim poder preencher os dados no comando **lancar** por exemplo.

### Cron

Existe a opção de criar uma cron para lançamento de horas em um determinado dia e hora.
Como ainda está em desenvolvimento, a melhor forma de entender é ler sobre o framework utilizado.

[Plan](https://github.com/fengsp/plan)

E essencialmente o que ele faz é gerar uma cron e escrever na sua crontab de usuário. (você usa linux claro!)

### Roadmap

- Monday Cronjob :thumbsup:  
  Hoje existe o rascunho de um algoritmo de cron que roda todo sábado e verifica se você lançou o horário da segunda. (aquele problema de esquecer de lançar as horas sabe?)
- Daily Cronjob  
  Uma cronjob capaz de consumir uma fonte e diariamente lançar as horas. 
- Import/Parser  
  Funcionalidade de importação de tabela com horas. Fontes como um csv ou até mesmo google sheets. 
