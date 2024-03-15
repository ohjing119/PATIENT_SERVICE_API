from sqlalchemy import Column, ForeignKey
from lib.models.model_base import ModelBase
from lib.models.hospital import Hospital

from sqlalchemy.orm import mapped_column, relationship

import sqlalchemy.dialects.postgresql as pg

class Department(ModelBase):
    __tablename__ = "Department"
    
    department_id = Column(
        pg.INTEGER,        
        primary_key=True,
        autoincrement=True
    )
    department_name = Column(pg.VARCHAR, unique=True, nullable=False)    
    hospital_id = mapped_column(pg.INTEGER, ForeignKey(Hospital.hospital_id), nullable=False)
    
    # relationships    
    hospital = relationship("Hospital", foreign_keys=[hospital_id])
   


