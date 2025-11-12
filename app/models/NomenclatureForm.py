from db.base import Base
from sqlalchemy import Column, Integer, String

class NomenclatureForm(Base):
    __tablename__ = "NomenclatureForm"

    id = Column(Integer, primary_key=True, index=True)
    CarModel = Column(String)
    VIN = Column(String)
    DataCarId = Column(String)
    car_guid = Column(String)
