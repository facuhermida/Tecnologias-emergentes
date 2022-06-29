from fastapi import FastAPI, APIRouter
import paho.mqtt.client as mqtt
import random
from datetime import date
from typing import Union
from config.database import conn
from models.models import datos, logs
from schema.dato import Dato
from schema.log import Log
from sqlalchemy.sql import text
#from schema.dato import Dato

appRouter = APIRouter()


@appRouter.get("/datos")
async def get_datos():
     return conn.execute(datos.select()).fetchall()


@appRouter.post("/datos/")
async def create_datos(dato: Dato):
    new_dato = {"ID": dato.id, "Temperatura": dato.temperatura, "Humedad": dato.humedad}
    conn.execute(datos.insert(new_dato))

#max_hum    min_temp    min_hum     temp_max_by_qty     hum_max_by_qty     temp_min_by_qty     hum_min_by_qty

@appRouter.get("/maxtemp")
async def max_temp():
    
    rs = conn.execute("SELECT * FROM datos ORDER BY Temperatura DESC LIMIT 1").fetchall()

    fecha = date.today().strftime("%d/%m/%Y")
    data = ({"Fecha": fecha, "Accion": "max_temp"})

    conn.execute(logs.insert(data))

    return rs

@appRouter.get("/maxhum")
async def max_hum():

    rs = conn.execute("SELECT * FROM datos ORDER BY Humedad DESC LIMIT 1").fetchall()

    fecha = date.today().strftime("%d/%m/%Y")
    data = ({"Fecha": fecha, "Accion": "max_hum"})

    conn.execute(logs.insert(data))

    #conn.execute("INSERT INTO logs(Fecha, Accion) VALUES(:fecha, :accion)")

    return rs
    
@appRouter.get("/mintemp")
async def min_temp():
    rs = conn.execute("SELECT * FROM datos ORDER BY Temperatura ASC LIMIT 1").fetchall()

    fecha = date.today().strftime("%d/%m/%Y")
    data = ({"Fecha": fecha, "Accion": "min_temp"})

    conn.execute(logs.insert(data))

    return rs

@appRouter.get("/minhum")
async def min_hum():

    rs = conn.execute("SELECT * FROM datos ORDER BY Humedad ASC LIMIT 1").fetchall()

    fecha = date.today().strftime("%d/%m/%Y")
    data = ({"Fecha": fecha, "Accion": "min_hum"})

    conn.execute(logs.insert(data))

    return rs

@appRouter.get("/temp_max_by_qty")
async def temp_max_by_qty():

    return conn.execute("SELECT * FROM logs WHERE Accion='max_temp'").fetchall()

@appRouter.get("/hum_max_by_qty")
async def hum_max_by_qty():

    return conn.execute("SELECT * FROM logs WHERE Accion='max_hum'").fetchall()

@appRouter.get("/temp_min_by_qty")
async def temp_min_by_qty():

    return conn.execute("SELECT * FROM logs WHERE Accion='min_temp'").fetchall()

@appRouter.get("/hum_min_by_qty")
async def hum_min_by_qty():

    return conn.execute("SELECT * FROM logs WHERE Accion='min_hum'").fetchall()