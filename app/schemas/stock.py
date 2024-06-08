from pydantic import BaseModel



class StockBaseSchema(BaseModel):
    weight: float
    description: str
    price: float


class StockCreateSchema(StockBaseSchema):
    pass


class StockCreateSchema2(StockBaseSchema):
    company_id: int
    product_id: int

    
class StockSchema(StockBaseSchema):
    id: int
    company_id: int
    product_id: int
