from sqlalchemy import Column
from lib.models.model_base import ModelBase
import sqlalchemy.dialects.postgresql as pg

class Room(ModelBase):
    __tablename__ = "room"
    
    room_id = Column(
        pg.INTEGER,        
        primary_key=True,
        autoincrement=True
    )

    room_type_name = Column(pg.VARCHAR)
    available = Column(pg.BOOLEAN, 
                       nullable=False, 
                       default=True)

