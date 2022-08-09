from fastapi import FastAPI, APIRouter
import paho.mqtt.client as mqtt
import random
from datetime import date
from typing import Union
from config.database import conn
from models.models import datos, logs
from schema.dato import Dato
from schema.log import Log
from sqlalchemy.sql import text, table, column
from routes.MQTT_publisher import publicar
from routes.MQTT_subscriber import subscribir
#from schema.dato import Dato

appRouter = APIRouter()


@appRouter.get("/datos")
async def get_datos():
     return conn.execute(datos.select()).fetchall()


@appRouter.post("/datos/")
async def create_datos(dato: Dato):

    fecha = date.today().strftime("%d/%m/%Y")

    new_dato = { "humedad": dato.humedad, "temperatura": dato.temperatura, "fecha": fecha, "longitud": dato.longitud, "latitud": dato.latitud}
    #conn.execute(datos.insert({ "humedad": dato.humedad, "temperatura": dato.temperatura, "fecha": fecha, "longitud": dato.longitud, "latitud": dato.latitud})
    conn.execute(table('datos', column('humedad'), column('temperatura'), column('fecha'), column('longitud'), column('latitud')).insert().values({ "humedad": dato.humedad, "temperatura": dato.temperatura, "fecha": fecha, "longitud": dato.longitud, "latitud": dato.latitud}))

    #Levantar proyecto en el server
    #publicar("Grupo2", new_dato)

#max_hum    min_temp    min_hum     temp_max_by_qty     hum_max_by_qty     temp_min_by_qty     hum_min_by_qty

@appRouter.get("/maxtemp")
async def max_temp():
    
    rs = conn.execute("SELECT * FROM datos ORDER BY Temperatura DESC LIMIT 1").fetchall()

   # publicar("Max temp", rs)

    return rs

@appRouter.get("/maxhum")
async def max_hum():

    rs = conn.execute("SELECT * FROM datos ORDER BY Humedad DESC LIMIT 1").fetchall()

    return rs
    
@appRouter.get("/mintemp")
async def min_temp():
    rs = conn.execute("SELECT * FROM datos ORDER BY Temperatura ASC LIMIT 1").fetchall()

    return rs

@appRouter.get("/minhum")
async def min_hum():

    rs = conn.execute("SELECT * FROM datos ORDER BY Humedad ASC LIMIT 1").fetchall()

    return rs

@appRouter.get("/temp_max_by_qty")
async def temp_max_by_qty(cantidad):

    return conn.execute("SELECT * FROM datos ORDER BY Temperatura DESC LIMIT "+cantidad).fetchall()

@appRouter.get("/hum_max_by_qty")
async def hum_max_by_qty(cantidad):

    return conn.execute("SELECT * FROM datos ORDER BY Humedad DESC LIMIT "+cantidad).fetchall()

@appRouter.get("/temp_min_by_qty")
async def temp_min_by_qty(cantidad):

    return conn.execute("SELECT * FROM datos ORDER BY Temperatura ASC LIMIT "+cantidad).fetchall()

@appRouter.get("/hum_min_by_qty")
async def hum_min_by_qty():

    return conn.execute("SELECT * FROM datos ORDER BY Humedad ASC LIMIT "+cantidad).fetchall()

@appRouter.get("/hum_by_location")
async def hum_by_location(latitud, longitud):

    return conn.execute("SELECT humedad FROM datos WHERE latitud = '"+ latitud +"' AND longitud = '"+longitud +"'  LIMIT 10").fetchall()

@appRouter.get("/temp_by_location")
async def temp_by_location(latitud, longitud):

    return conn.execute("SELECT temperatura FROM datos WHERE latitud = '"+ latitud +"' AND longitud = '"+longitud +"' LIMIT 10").fetchall()
