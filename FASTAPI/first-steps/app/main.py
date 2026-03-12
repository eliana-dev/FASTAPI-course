from fastapi import FastAPI
from app.core.db import Base, engine
from app.api.v1.posts.router import router as post_router
# import uvicorn


def create_app() -> FastAPI:
    app = FastAPI(title="Mini Blog")
    Base.metadata.create_all(bind=engine)
    app.include_router(post_router)
    return app

app= create_app()

# if __name__ == "__main__":
#     uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
