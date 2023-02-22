from fastapi import FastAPI
from uvicorn import run

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


def run_server():
    run(app, host="127.0.0.1", port=8000)


if __name__ == "__main__":
    run_server()
