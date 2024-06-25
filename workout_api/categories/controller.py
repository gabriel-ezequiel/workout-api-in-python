from uuid import uuid4
from fastapi import APIRouter, status, Body, HTTPException
from workout_api.categories.models import CategoryModel
from workout_api.categories.schemas import CategoryIn, CategoryOut
from workout_api.contrib.dependencies import DatabaseDependency
from sqlalchemy.future import select
from pydantic import UUID4

router = APIRouter()

@router.post(path="/", summary="Create a new category", status_code=status.HTTP_201_CREATED, response_model=CategoryOut,)
async def post(db_session: DatabaseDependency, category_in: CategoryIn = Body(...)) -> CategoryOut:
    category_out = CategoryOut(id=uuid4(), **category_in.model_dump())
    category_model = CategoryModel(**category_out.model_dump())
    
    db_session.add(category_model)
    await db_session.commit()

    return category_out

@router.get(path="/", summary="Get all categories", status_code=status.HTTP_200_OK, response_model=list[CategoryOut])
async def query(db_session: DatabaseDependency,) -> list[CategoryOut]:
    categories: list[CategoryOut] = (await db_session.execute(select(CategoryModel))).scalars().all()
     
    return categories

@router.get(path="/{id}", summary="Get a category by id", status_code=status.HTTP_200_OK, response_model=CategoryOut,)
async def query(id: UUID4, db_session: DatabaseDependency) -> CategoryOut:
    category: CategoryOut = (await db_session.execute(select(CategoryModel).filter_by(id=id))).scalars().first()

    if not category:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Category not found")
    
    return category