import datetime
import uuid
from sqlalchemy import Column, ForeignKey
from lib.models.model_base import ModelBase
from lib.models.physician import Physician
from sqlalchemy.orm import mapped_column, relationship
import sqlalchemy.dialects.postgresql as pg

class Patient(ModelBase):
    __tablename__ = "patient"
    patient_record_number = Column(
        pg.BIGINT,
        primary_key=True,
        autoincrement=True,
        nullable=False
    )
    first_name = Column(pg.VARCHAR)
    last_name = Column(pg.VARCHAR)
    ssn = Column(pg.VARCHAR, nullable=False)
    dob = Column(pg.DATE)
    gender = Column(pg.VARCHAR)
    mailing_address = Column(pg.VARCHAR)
    physician_id = mapped_column(pg.INTEGER, ForeignKey(Physician.physician_id), nullable=False)
    insurance_id = Column(pg.INTEGER)

    # relationships
    physician = relationship("Physician", foreign_keys=[physician_id])