from db.base import Base
from sqlalchemy import Column, Integer, String

class Company(Base):
    __tablename__ = "companies"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=True)
    fullName = Column(String, nullable=True)
    inn = Column(String, nullable=True)
    kpp = Column(String, nullable=True)
    ogrn = Column(String, nullable=True)
    company_guid = Column(String, nullable=True)
