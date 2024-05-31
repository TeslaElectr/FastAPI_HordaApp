from pydantic import BaseModel
from pydantic import Field


class ProductBaseSchema(BaseModel):
    name: str
    description: str


class ProductCreateSchema(ProductBaseSchema):
    pass 


class ProductCreateSchema2(ProductBaseSchema):
    company_id: int 
    type_id: int 

    
class ProductSchema(ProductBaseSchema):
    id: int
    company_id: int 
    type_id: int 

    
