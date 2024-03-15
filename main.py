from fastapi import FastAPI
from lib.db_session_maker import SessionMaker
from lib.models.patient import Patient
from lib.models.physician import Physician

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/patients")
async def get_patients():
    db_session = SessionMaker().get_session_maker()
    with db_session.begin() as session:
        patients = session.query(Patient).all()
    return patients

@app.get("/physicians")
async def get_physicians():
    db_session = SessionMaker().get_session_maker()
    with db_session.begin() as session:
        physicians = session.query(Physician).all()
    return physicians