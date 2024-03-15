from sqlalchemy import Column
from lib.models.model_base import ModelBase
import sqlalchemy.dialects.postgresql as pg

class Physician(ModelBase):
    __tablename__ = "physician"
    physician_id = Column(
        pg.INTEGER,
        primary_key=True,
        autoincrement=True,
        nullable=False
    )
    first_name = Column(pg.VARCHAR)
    last_name = Column(pg.VARCHAR)
    ssn = Column(pg.VARCHAR, nullable=False)
