from pydantic import BaseModel
from pydantic import EmailStr
# from pydantic import Field

class CompanyBaseSchema(BaseModel):
    name: str
    city: str
    inn: int | None
    kpp: int
    address: str
    phone: int | None
    email: EmailStr | None


class CompanyCreateSchema(CompanyBaseSchema):
    pass

    
class CompanySchema(CompanyBaseSchema):
    id: int
