from fastapi import FastAPI
from app.api.v1.endpoints.auth import router as auth_router

# Run this once to create tables in the database
from app.db.session import engine, Base
from app.models.user import User

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(auth_router, prefix="/api/v1/auth")
