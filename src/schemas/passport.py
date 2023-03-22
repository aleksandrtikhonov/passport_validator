from fastapi.params import Query
from pydantic import BaseModel


class Passport(BaseModel):
    seria: str = Query(default=None, max_length=4)
    number: str = Query(default=None, max_length=6)
