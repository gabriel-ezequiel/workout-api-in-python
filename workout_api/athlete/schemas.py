from typing import Annotated, Optional
from pydantic import Field, PositiveFloat
from workout_api.categories.schemas import CategoryIn
from workout_api.contrib.schemas import BaseSchema, OutMixin
from workout_api.training_center.schemas import TrainingCenterAthlete

class Athlete(BaseSchema):
    name: Annotated[str, Field(description="The name of the athlete", example="John", max_length=50)]
    cpf: Annotated[str, Field(description="The CPF of the athlete", example="12345678900", max_length=11)]
    age: Annotated[int, Field(description="The age of the athlete", example=25)]
    weight: Annotated[PositiveFloat, Field(description="The weight of the athlete", example=70.5)]
    height: Annotated[PositiveFloat, Field(description="The height of the athlete", example=1.75)]
    gender: Annotated[str, Field(description="The gender of the athlete", example="M", max_length=1)]
    category: Annotated[CategoryIn, Field(description="The category of the athlete")]
    training_center: Annotated[TrainingCenterAthlete, Field(description="The training center of the athlete")]

class AthleteIn(Athlete):
    pass

class AthleteOut(Athlete, OutMixin):
    pass

class AthleteUpdate(BaseSchema):
    name: Annotated[Optional[str], Field(None, description="The name of the athlete", example="John", max_length=50)]
    age: Annotated[Optional[int], Field(None, description="The age of the athlete", example=25)]