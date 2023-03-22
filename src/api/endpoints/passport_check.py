from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse


from models.memory_db import passport_memory_db
from schemas.passport import Passport

passport_router = APIRouter()


@passport_router.get('/one_instance/', summary='Проверка одной записи', response_model=Passport)
async def fast_check_one_passport(passport_data: Passport = Depends()) -> JSONResponse:
    """Проверить номер документа в базе недействительных паспортов"""
    passport_full_number = passport_data.seria + passport_data.number
    return JSONResponse({passport_full_number: int(passport_data.number) in passport_memory_db[passport_data.seria]})
