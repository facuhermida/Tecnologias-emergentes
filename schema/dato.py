from pickletools import long1
from pydantic import BaseModel
from typing import Optional
class Dato(BaseModel):

    id: Optional[int]
    fecha: str
    temperatura: float
    humedad: float
    latitud: int
    longitud: int
