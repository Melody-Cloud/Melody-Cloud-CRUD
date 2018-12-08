from flask_peewee.rest import PostgresqlDatabase

# pgdb = PostgresqlDatabase('postgres', user='postgres', password='admin', host='localhost', port=5432)
pgdb = PostgresqlDatabase('postgres', user='postgres', password='postgres', host='melody-cloud-database.cwlxotwollvs.eu-west-1.rds.amazonaws.com', port=5432)
