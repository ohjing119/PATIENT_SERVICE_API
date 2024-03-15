from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import orm

Base = declarative_base()

class ModelBase(Base):
    __abstract__ = True
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.on_load(**kwargs)

    # this will automatically set attributes if passed into the constructor
    @orm.reconstructor
    def on_load(self, **kwargs) -> None:
        print (kwargs)
        for (k, v) in kwargs.items():
            if v is not None:
                setattr(self, k, v)

    def to_dict(self):
        data_dict = self.__dict__
        del data_dict['_sa_instance_state']
        return data_dict
