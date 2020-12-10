from db.record_db import RecordInDB
from db.record_db import save_record, get_record

from models.record_models import RecordIn, RecordOut

import datetime
from fastapi import FastAPI
from fastapi import HTTPException 

api = FastAPI()

@api.post("/record/auth/") 