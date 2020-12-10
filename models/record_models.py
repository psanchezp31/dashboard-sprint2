##################imports##################################

from pydantic import BaseModel              #validación de datos (?)
from datetime import datetime               #función para el tipo de dato DATE, DATETIME

class RecordIn (BaseModel):
    id: int = 0 
    categoria: str
    tipo: str 
    cantidad: int
    fecha_registro: datetime = datetime.now() #revise

class RecordOut (BaseModel):
    id: int = 0 
    categoria: str
    tipo: str 
    cantidad: int
    fecha_registro: datetime = datetime.now() #revise