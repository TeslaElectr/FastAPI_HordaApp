from pydantic import BaseModel


class RecipeBaseSchemas(BaseModel):
    recipe: dict

    
class RecipeCreateSchema(RecipeBaseSchemas):
    pass 


class RecipeSchema(RecipeBaseSchemas):
    id :int
    