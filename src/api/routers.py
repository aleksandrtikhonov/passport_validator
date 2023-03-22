from fastapi import APIRouter

from api.endpoints.passport_check import passport_router
from api.endpoints.site import site_router

# from api.endpoints.passport_check import passport_router
# from api.endpoints.site import site_router

main_router = APIRouter()

main_router.include_router(
    passport_router,
    prefix='/check',
    tags=['Passport check'],
)

main_router.include_router(site_router, tags=['Main page'])
