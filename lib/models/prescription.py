from sqlalchemy import Column, ForeignKey
from sqlalchemy.orm import mapped_column, relationship

from lib.models.model_base import ModelBase
from lib.models.medication import Medication
from lib.models.physician import Physician
from lib.models.patient import Patient

import sqlalchemy.dialects.postgresql as pg

class Prescription(ModelBase):
    __tablename__ = "prescription"
    prescription_id = Column(
        pg.INTEGER,
        primary_key=True,
        autoincrement=True,
        nullable=False
    )
    medication_id = mapped_column(pg.INTEGER, ForeignKey(Medication.medication_id), nullable=False)
    physician_id = mapped_column(pg.INTEGER, ForeignKey(Physician.physician_id), nullable=False)
    patient_id = mapped_column(pg.INTEGER, ForeignKey(Patient.patient_record_number), nullable=False)
    
# relationships
    medication = relationship("Medication", foreign_keys=[medication_id])
    physician = relationship("Physician", foreign_keys=[physician_id])
    patient = relationship("Patient", foreign_keys=[patient_id])
