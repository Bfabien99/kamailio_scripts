# KAMAILIO SCRIPTS

Contient un ensemble de script pour me permettre de faire communiquer kamailio avec la base de donnée postgreSQL au travers de python

## requirements

### Pour la base de données

J'utilise [psycopg](https://www.psycopg.org/install/) pour la connexion à la base de donnée postgreSQL


## le fichier configs

Il y a le fichier de configuration, configs.py, qui n'a pas été commite... C'est fait exprès.
Ce fichier contient nos données confidentielles tels que les identifiants de connexion à la base de données.

## structure du fichier configs
```
import psycopg

dbuser = "username"
dbname = "dbname"
dbport = 0000
dbhost = "localhost"
dbpassword = "securepassword"
connection_url = f"postgresql://{dbuser}:{dbpassword}@{dbhost}:{dbport}/{dbname}"
```