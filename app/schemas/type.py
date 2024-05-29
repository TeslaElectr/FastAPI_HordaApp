from pydantic import BaseModel

class TypeBaseSchema(BaseModel):
    name: str
    description: str

    
class TypeCreateSchema(TypeBaseSchema):
    pass


class TypeSchema(TypeBaseSchema):
    id :int