from curses import meta
from sqlalchemy import Table, Boolean, Column, ForeignKey, Integer, String, Float
from sqlalchemy.orm import relationship
from config.database import meta, engine



datos = Table("datos", meta, Column(
    "ID", Integer, primary_key=True), 
    Column("Temperatura", Float), 
    Column("Humedad", Float))

logs = Table("logs", meta, Column(
    "ID", Integer, primary_key=True),
    Column("Fecha", String(15)),
    Column("Accion", String(45))
    
)

meta.create_all(engine)

# class Datos(Base):
#     __tablename__ = "datos"

#     id = Column(Integer, primary_key=True, index=True)
#     temperatura = Column(Float, unique=True, index=True)
#     humedad = Column(Float)
