from fastapi import FastAPI
from sqlalchemy import text

from app.database import SessionLocal
from app.redis_client import redis_client

app = FastAPI()


@app.get("/")
def root():
    return {
        "message": "FastAPI funcionando"
    }


@app.get("/db")
def test_database():

    db = SessionLocal()

    try:
        result = db.execute(text("SELECT NOW()"))
        current_time = result.scalar()

        return {
            "database": "PostgreSQL",
            "time": current_time
        }

    finally:
        db.close()


@app.get("/redis")
def test_redis():

    redis_client.set("test_key", "Hola desde FastAPI")

    value = redis_client.get("test_key")

    return {
        "redis": value
    }