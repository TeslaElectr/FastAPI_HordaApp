from pydantic import BaseModel


class ProductionBaseSchema(BaseModel):
    address: str
    description: str

    
class ProductCreateSchema(ProductionBaseSchema):
    pass 


class ProductSchema(ProductionBaseSchema):
    id: int