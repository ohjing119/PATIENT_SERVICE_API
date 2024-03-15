from sqlalchemy import Column
from lib.models.model_base import ModelBase
import sqlalchemy.dialects.postgresql as pg

class Appointment(ModelBase):
    __tablename__ = "appointment"
    appointment_id = Column(
        pg.INTEGER,
        primary_key=True,
        autoincrement=True,
        nullable=False
    )
    patient_record_number = Column(pg.INTEGER, nullable=False)
    medication_name = Column(pg.VARCHAR, nullable= False)
    # nurse_id
    physician_id = Column(pg.INTEGER, nullable=False)
    start_date_time = Column(pg.TIMESTAMP)
    end_date_time = Column(pg.TIMESTAMP)
    exam_room_id = Column(pg.INTEGER)