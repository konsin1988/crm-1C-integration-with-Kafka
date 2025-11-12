from db.base import Base
from sqlalchemy import Column, Integer, String

class DataFormCar(Base):
    __tablename__ = "DataFormCar"

    id = Column(Integer, primary_key=True, index=True)
    ClientId = Column(Integer)
    DogovorNumber = Column(String, nullable=True)
