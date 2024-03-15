from sqlalchemy import Column
from lib.models.model_base import ModelBase
import sqlalchemy.dialects.postgresql as pg

class Hospital(ModelBase):
    __tablename__ = "Hospital"
    
    hospital_id = Column(
        pg.INTEGER,        
        primary_key=True,
        autoincrement=True
    )
    hospital_name = Column(pg.VARCHAR, unique=True, nullable=False)    
     


