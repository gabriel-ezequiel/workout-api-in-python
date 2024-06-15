from typing import Annotated
from pydantic import BaseModel, UUID4, Field
from datetime import datetime


class BaseSchema(BaseModel):
    class Config:
        extra = 'forbid'
        from_attriubtes = True


class OutMixin(BaseSchema):
    id: Annotated[UUID4, Field(description="The UUID of the object")]
    created_at: Annotated[datetime, Field(description="The date of the object creation")]