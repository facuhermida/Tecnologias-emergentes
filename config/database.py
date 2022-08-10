import json
from sqlalchemy import create_engine, MetaData, insert
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import text, table, column

#engine = create_engine("mysql+pymysql://root:MySQLTECEm$2022@137.184.200.34:3306/tecnologias_emergentes")
engine = create_engine("mysql+pymysql://root:MySQLTECEm$2022@localhost:3306/pilarGrupo2")

meta = MetaData()

conn = engine.connect()

# def insert_datos(jsonData):
#     datos = json.loads(jsonData)
#     fecha = datos['fecha']
#     temperatura = datos['temperatura']
#     humedad = datos['humedad']
#     latitud = datos['latitud']
#     longitud = datos['longitud']

#     conn.execute(table('datos', column('humedad'), column('temperatura'), column('fecha'), column('longitud'), column('latitud')).insert().values({ "humedad": humedad, "temperatura": temperatura, "fecha": fecha, "longitud": longitud, "latitud": latitud}))

#     print("Datos insertados")
