import time
from pathlib import Path

from fastapi import FastAPI
from uvicorn import run

from api.routers import main_router
from loader import load_memory_db_from_local_file
from models.memory_db import passport_memory_db


file = Path('../media/suka.txt.gz')

app = FastAPI()
app.include_router(main_router)

# Для эмуляции загрузки файла.
# @app.get("/file.zip.gz")
# @app.head("/file.zip.gz")
# async def root() -> FileResponse:
#     return FileResponse(file)


@app.on_event('startup')
async def startup() -> None:
    t1 = time.time()
    passport_memory_db.update(load_memory_db_from_local_file())

    print(f"В память залетело за {time.time() - t1:0f} sec")


def run_server(app: FastAPI) -> None:
    run(app, host="0.0.0.0", port=8000)


if __name__ == "__main__":
    run_server(app)
