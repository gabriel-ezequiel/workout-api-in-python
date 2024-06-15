from fastapi import APIRouter
from workout_api.athlete.controller import router as athlete

api_router = APIRouter()
api_router.include_router(athlete, prefix='/athletes', tags=['athletes'])


