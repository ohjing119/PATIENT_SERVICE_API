from sqlalchemy import Column
from lib.models.model_base import ModelBase
import sqlalchemy.dialects.postgresql as pg

class RoomType(ModelBase):
    __tablename__ = "room_type"
    room_type_id = Column(
        pg.VARCHAR,
        primary_key=True,
        autoincrement=True
    )    
    room_type_name = Column(pg.VARCHAR, unique=True)
    