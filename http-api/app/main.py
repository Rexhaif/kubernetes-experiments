from fastapi import FastAPI
from redis import Redis
from .config import settings

app = FastAPI()
redis = Redis(host=settings.redis.host, port=settings.redis.port)

@app.get("/set")
def set_redis(key: str, value: str):
    result = redis.set(key, value)
    return {"result": result}

@app.get("/get")
def get_redis(key: str):
    result = redis.get(key)
    return {"result": result}