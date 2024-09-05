import uvicorn
from fastapi import FastAPI
from api import router as api_router
from core.config import settings

app = FastAPI()
app.include_router(api_router, prefix=settings.api.prefix)


@app.get("/")
def get_hello():
    return "Hello world!"


if __name__ == "__main__":
    uvicorn.run("main:app", host=settings.run.host, port=settings.run.port, reload=True)
