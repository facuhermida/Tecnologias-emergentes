from pydantic import BaseModel
from typing import Text

class Datos(BaseModel):
    id: int
    temperatura: float
    humedad: float

