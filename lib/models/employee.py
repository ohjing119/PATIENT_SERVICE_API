from sqlalchemy import Column, ForeignKey
from lib.models.model_base import ModelBase
import sqlalchemy.dialects.postgresql as pg
from lib.models.department import Department

from sqlalchemy.orm import mapped_column, relationship

class Employee(ModelBase):
    __tablename__ = "employee"
    employee_id = Column(
        pg.INTEGER,
        primary_key=True,
        autoincrement=True
    )
    first_name = Column(pg.VARCHAR)
    last_name = Column(pg.VARCHAR)
    ssn = Column(pg.VARCHAR, nullable=False)
    title = Column(pg.VARCHAR)
    gender = Column(pg.VARCHAR, nullable=False)
    email = Column(pg.VARCHAR)
    hire_date = Column(pg.DATE)
    department_id = mapped_column(pg.INTEGER, ForeignKey(Department.department_id), nullable=False)
    
    # relationships    
    department = relationship("Department", foreign_keys=[department_id])
   

