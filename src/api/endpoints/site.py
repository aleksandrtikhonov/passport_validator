from fastapi import APIRouter
from starlette.requests import Request
from starlette.responses import HTMLResponse
from starlette.templating import Response, Jinja2Templates

site_router = APIRouter()
templates = Jinja2Templates(directory="../front/")


@site_router.get('/', response_class=HTMLResponse)
async def index(request: Request) -> Response:
    return templates.TemplateResponse("index.html", {"request": request})
