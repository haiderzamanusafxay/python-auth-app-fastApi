from pydantic import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str = "mysql+pymysql://haider:password@localhost:3306/fastapi_blog"

settings = Settings()
