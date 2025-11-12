from pydantic import BaseModel
from typing import Optional

class Company(BaseModel):
    id: int
    name: str
    fullName: str | None = None
    inn: str | None = None
    kpp: str | None = None
    ogrn: str | None = None
    company_guid: str | None = None

    class Config:
        orm_mode = True
