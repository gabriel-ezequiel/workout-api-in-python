from typing import Annotated
from pydantic import Field, UUID4
from workout_api.contrib.schemas import BaseSchema

class TrainingCenterIn(BaseSchema):
    name: Annotated[str, Field(description="The name of the training center", example="Training Center", max_length=20)]
    address: Annotated[str, Field(description="The address of the training center", example="Street, 123", max_length=60)]
    owner: Annotated[str, Field(description="The owner of the training center", example="John Doe", max_length=30)]

class TrainingCenterAthlete(BaseSchema):
    name: Annotated[str, Field(description="The name of the training center", example="Training Center", max_length=20)]

class TrainingCenterOut(TrainingCenterIn):
    id: Annotated[UUID4, Field(description="The identifier of the training center")]