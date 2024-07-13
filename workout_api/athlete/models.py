import datetime
from sqlalchemy import DateTime, ForeignKey, Integer, String, Float
from sqlalchemy.orm import Mapped, mapped_column, relationship
from workout_api.contrib.models import BaseModel


class AthleteModel(BaseModel):
    __tablename__ = 'athletes'

    pk_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(50), nullable=False)
    cpf: Mapped[str] = mapped_column(String(11), nullable=False, unique=True)
    age: Mapped[int] = mapped_column(Integer, nullable=False)
    weight: Mapped[float] = mapped_column(Float, nullable=False)
    height: Mapped[float] = mapped_column(Float, nullable=False)
    gender: Mapped[str] = mapped_column(String(1), nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime, nullable=False)
    category: Mapped['CategoryModel'] = relationship(back_populates='athletes', lazy='selectin')
    category_id: Mapped[int] = mapped_column(ForeignKey('categories.pk_id'), nullable=False)
    training_center: Mapped['TrainingCenterModel'] = relationship(back_populates='athletes', lazy='selectin')
    training_center_id: Mapped[int] = mapped_column(ForeignKey('training_center.pk_id'), nullable=False)
    