from sqlalchemy import Column
from lib.models.model_base import ModelBase
import sqlalchemy.dialects.postgresql as pg

class Medication(ModelBase):
    __tablename__ = "medication"
    medication_id = Column(
        pg.INTEGER,
        primary_key=True,
        autoincrement=True,
        nullable=False
    )
    medication_name = Column(pg.VARCHAR, nullable= False)
    brand = Column(pg.VARCHAR)
    medication_desc = Column(pg.VARCHAR, nullable=False)
