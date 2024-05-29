from pydantic import BaseModel


class ProductionBaseSchema(BaseModel):
    address: str
    description: str
    weight_product: float
    weight_stock: float

    
class ProductionCreateSchema(ProductionBaseSchema):
    pass 


class ProductionSchema(ProductionBaseSchema):
    id: int