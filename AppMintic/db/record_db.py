##################imports##################################

from typing import Dict             #tipado de datos (ej: str, int, boolean, etc.)
from pydantic import BaseModel      #validación de datos (?)
from datetime import datetime       #función para el tipo de dato DATE, DATETIME

###########definición de el objeto record##################

class RecordInDB(BaseModel):
    id: int = 0                                 #AUTOINCREMENTAL
    categoria: str                              #e.g. HEALTH, PETS, FOOD, SALARY
    tipo: str                                   #EXPENSES OR INCOME
    cantidad: int                               #e.g. $ 150.000
    fecha_registro: datetime = datetime.now()   #revise

#################base de datos################################

database_records = []
database_records = {

}

##############métodos para el POST y el GET###################

generator ={"id"=0}                         #AUTOINCREMENTAL

def save_record(record_in_db: RecordInDB):  #CREATE RECORD (POST)
    generator["id"] = generator ["id"] + 1 
    record_in_db.id = generator["id"]
    database_records.append(record_in_db)
    return record_in_db

def get_record():                           #READ RECORD (GET)
    if categoria in database_records.keys():
        return database_records[categoria]
    else:
        return None




