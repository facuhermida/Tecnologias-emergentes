from pydantic import BaseModel
from typing import Optional
class Dato(BaseModel):

    id: Optional[int]
    temperatura: float
    humedad: float