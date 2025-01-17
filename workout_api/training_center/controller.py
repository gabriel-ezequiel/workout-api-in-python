from uuid import uuid4
from fastapi import APIRouter, status, Body, HTTPException
from workout_api.training_center.models import TrainingCenterModel
from workout_api.training_center.schemas import TrainingCenterIn, TrainingCenterOut
from workout_api.contrib.dependencies import DatabaseDependency
from sqlalchemy.future import select
from pydantic import UUID4

router = APIRouter()

@router.post(path="/", summary="Create a new trainig center", status_code=status.HTTP_201_CREATED, response_model=TrainingCenterOut,)
async def post(db_session: DatabaseDependency, training_center_in: TrainingCenterIn = Body(...)) -> TrainingCenterOut:
    training_center_out = TrainingCenterOut(id=uuid4(), **training_center_in.model_dump())
    training_center_model = TrainingCenterModel(**training_center_out.model_dump())
    
    db_session.add(training_center_model)
    await db_session.commit()

    return training_center_out

@router.get(path="/", summary="Get all trainig center", status_code=status.HTTP_200_OK, response_model=list[TrainingCenterOut])
async def query(db_session: DatabaseDependency,) -> list[TrainingCenterOut]:
    training_centers: list[TrainingCenterOut] = (await db_session.execute(select(TrainingCenterModel))).scalars().all()
     
    return training_centers

@router.get(path="/{id}", summary="Get a trainig center by id", status_code=status.HTTP_200_OK, response_model=TrainingCenterOut,)
async def query(id: UUID4, db_session: DatabaseDependency) -> TrainingCenterOut:
    training_center: TrainingCenterOut = (await db_session.execute(select(TrainingCenterModel).filter_by(id=id))).scalars().first()

    if not training_center:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="training_center not found")
    
    return training_center