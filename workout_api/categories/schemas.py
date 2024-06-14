from typing import Annotated
from pydantic import Field
from workout_api.contrib.schemas import BaseSchema

class Category(BaseSchema):
    name: Annotated[str, Field(description="The name of the category", example="Scale", max_length=10)]