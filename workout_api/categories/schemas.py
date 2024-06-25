from typing import Annotated
from pydantic import Field, UUID4
from workout_api.contrib.schemas import BaseSchema

class CategoryIn(BaseSchema):
    name: Annotated[str, Field(description="The name of the category", example="Scale", max_length=10)]

class CategoryOut(CategoryIn):
    id: Annotated[UUID4, Field(description="The identifier of the category")]