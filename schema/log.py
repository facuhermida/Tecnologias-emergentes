from pydantic import BaseModel
from typing import Optional
class Log(BaseModel):

    id: Optional[int]
    fecha: str
    accion: str