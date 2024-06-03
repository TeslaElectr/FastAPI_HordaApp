from pydantic import BaseModel


class RecipeBaseSchemas(BaseModel):
    recipe: dict

    class Config:
        orm_mode = True

    
class RecipeCreateSchema(RecipeBaseSchemas):
    pass 


class RecipeSchema(RecipeBaseSchemas):
    id :int
    