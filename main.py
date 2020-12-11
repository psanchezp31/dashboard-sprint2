from db.record_db import RecordInDB
from db.record_db import save_record, get_record

from models.record_models import RecordIn, RecordOut

import datetime
from fastapi import FastAPI
from fastapi import HTTPException 

api = FastAPI()

@api.get("/record/balance/{id}")
async def get_balance(id:int):
    record_in_db = get_record(id)
    if record_in_db == None:
        raise HTTPException(status_code=404, detail="El balance no existe")
    record_out=RecordOut(**record_in_db.dict())
    return record_out