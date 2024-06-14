from typing import Annotated
from pydantic import Field, PositiveFloat
from workout_api.contrib.schemas import BaseSchema

class Athlete(BaseSchema):
    name: Annotated[str, Field(description="The name of the athlete", example="John", max_length=50)]
    cpf: Annotated[str, Field(description="The CPF of the athlete", example="12345678900", max_length=11)]
    age: Annotated[int, Field(description="The age of the athlete", example=25)]
    weight: Annotated[PositiveFloat, Field(description="The weight of the athlete", example=70.5)]
    height: Annotated[PositiveFloat, Field(description="The height of the athlete", example=1.75)]
    gender: Annotated[str, Field(description="The gender of the athlete", example="M", max_length=1)]