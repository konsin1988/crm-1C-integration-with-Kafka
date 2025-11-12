from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models.DataFormCar import DataFormCar
from models.companies import Company 
from models.NomenclatureForm import NomenclatureForm


async def get_car_data(db: AsyncSession, id: int) : 
    result = await db.execute(select(DataFormCar).where(DataFormCar.id == id))
    dataFormCar_data = result.scalar_one_or_none()
    result = await db.execute(select(Company).where(Company.id == dataFormCar_data.ClientId))
    company_data = result.scalar_one_or_none().as_dict()
    result = await db.execute(select(NomenclatureForm).where(NomenclatureForm.DataCarId == id))
    nomenclature_items = [x.as_dict() for x in result.scalars().all()]

    company_data["DogovorNumber"] = dataFormCar_data.DogovorNumber
    company_data["id"] = id
    company_data["NomenclatureItems"] = nomenclature_items

    return company_data 

