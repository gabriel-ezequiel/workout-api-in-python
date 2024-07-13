from datetime import datetime
from fastapi import APIRouter, status, Body, HTTPException
from workout_api.athlete.schemas import AthleteIn, AthleteOut, AthleteUpdate
from workout_api.athlete.models import AthleteModel
from workout_api.categories.models import CategoryModel
from workout_api.contrib.dependencies import DatabaseDependency
from sqlalchemy.future import select
from uuid import uuid4

from workout_api.training_center.models import TrainingCenterModel

router = APIRouter()

@router.post(path="/", summary="Create a new athlete", status_code=status.HTTP_201_CREATED, response_model=AthleteOut)
async def post(db_session: DatabaseDependency, athlete_in: AthleteIn = Body(...)):
    category = (await db_session.execute(select(CategoryModel).filter_by(name=athlete_in.category.name))).scalars().first()

    if not category:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"Category not found with name {athlete_in.category.name}")
    
    training_center = (await db_session.execute(select(TrainingCenterModel).filter_by(name=athlete_in.training_center.name))).scalars().first()

    if not training_center:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"Training center not found with name {athlete_in.training_center.name}")

    try:
        athlete_out = AthleteOut(id=uuid4(), created_at=datetime.utcnow(), **athlete_in.model_dump())

        athlete_model = AthleteModel(**athlete_out.model_dump(exclude={'category', 'training_center'}))
        athlete_model.category_id = category.pk_id
        athlete_model.training_center_id = training_center.pk_id

        db_session.add(athlete_model)
        await db_session.commit()
    except Exception:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="An error occurred inserting the data into the database")

    return athlete_out

@router.get(path="/", summary="List all athletes", status_code=status.HTTP_200_OK, response_model=list[AthleteOut],)
async def query(db_session: DatabaseDependency) -> list[AthleteOut]:
    athletes: list[AthleteOut] = (await db_session.execute(select(AthleteModel))).scalars().all()

    return athletes

@router.get(path="/{id}", summary="Get an athlete by ID", status_code=status.HTTP_200_OK, response_model=AthleteOut,)
async def get(id: str, db_session: DatabaseDependency) -> AthleteOut:
    athlete: AthleteOut = (await db_session.execute(select(AthleteModel).filter_by(id=id))).scalars().first()

    if not athlete:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Athlete not found with ID {id}")

    return athlete

@router.patch(path="/{id}", summary="Update an athlete by ID", status_code=status.HTTP_200_OK, response_model=AthleteOut,)
async def get(id: str, db_session: DatabaseDependency, athlete_up: AthleteUpdate = Body(...)) -> AthleteOut:
    athlete: AthleteOut = (await db_session.execute(select(AthleteModel).filter_by(id=id))).scalars().first()

    if not athlete:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Athlete not found with ID {id}")
    
    athlete_update = athlete_up.model_dump(exclude_unset=True)
    
    for key, value in athlete_update.items():
        setattr(athlete, key, value)

    await db_session.commit()
    await db_session.refresh(athlete)

    return athlete

@router.delete(path="/{id}", summary="Delete an athlete by ID", status_code=status.HTTP_204_NO_CONTENT,)
async def get(id: str, db_session: DatabaseDependency) -> None:
    athlete: AthleteOut = (await db_session.execute(select(AthleteModel).filter_by(id=id))).scalars().first()

    if not athlete:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Athlete not found with ID {id}")
    
    await db_session.delete(athlete)
    await db_session.commit()
