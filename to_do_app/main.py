import uvicorn
from fastapi import FastAPI

from to_do_app.db.engine import Base, engine
from to_do_app.handlers.items import router as items_router

app = FastAPI()

app.include_router(items_router)

Base.metadata.create_all(bind=engine)


@app.get("/")
async def root():
    return {"message": "Hello World"}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
