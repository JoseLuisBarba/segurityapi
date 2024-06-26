from core.config import settings
from core.router import router
from routers import users
from db.mysql import engine, Base


from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

app = FastAPI(
    title = settings.PROJECT_NAME,
    openapi_url = f"{settings.API_V1_STR}/openapi.json"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.BACKEND_CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router, prefix = settings.API_V1_STR)

@app.on_event("startup")
async def startup():
    # create db tables
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)
        pass

if __name__ == "__main__":
    uvicorn.run("main:app", host=settings.HOST, port=settings.PORT)
