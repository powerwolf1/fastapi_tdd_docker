"""docstring"""
from fastapi import FastAPI, Depends

from config import get_settings, Settings


app = FastAPI()


@app.get('/')
async def root():
    """docstring"""
    return {'message': 'Hello world!'}


@app.get("/ping")
async def pong(settings: Settings = Depends(get_settings)):
    """docstring"""
    return {
        'ping': 'pong',
        'environment': settings.environment,
        'testing': settings.testing
    }
