
fun time

vamos a realizar varios ejercicios 


Section 1: API

In the context of a DB migration with 3 different tables (departments, jobs, employees) , create
a local REST API that must:

1. Receive historical data from CSV files
2. Upload these files to the new DB
3. Be able to insert batch transactions (1 up to 1000 rows) with one request

You need to publish your code in GitHub. It will be taken into account if frequent updates are
made to the repository that allow analyzing the development process. Ideally, create a
markdown file for the Readme.md
Clarifications
● You decide the origin where the CSV files are located.
● You decide the destination database type, but it must be a SQL database.
● The CSV file is comma separated.

------

### explicacion del condigo creado ###

main.py >> es el archivo principal que se ejecuta para correr el programa.

list_tables.py >> es el archivo que contiene la clase ListTables que se encarga de listar las tablas de la base de datos.

query1.py >> es el archivo que contiene la primera pregunta del ejercio,  se encarga de realizar las consultas a la base de datos.

query2.py >> es el archivo que contiene la segunda pregunta del ejercio,  se encarga de realizar las consultas a la base de datos.

resultados >> es el archivo que contiene los resultados de las consultas realizadas en el ejercicio.

###

ingesta_masiva.py >> es el archivo que contiene la clase IngestaMasiva que se encarga de realizar la ingesta masiva de datos a la base de datos.

prueba.csv >> es el archivo que contiene los datos que se van a ingresar a la base de datos.
