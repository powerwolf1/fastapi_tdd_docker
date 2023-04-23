"""docstring"""

import logging

from fastapi import Depends, FastAPI

from app.api import ping, summaries

from .config import Settings, get_settings
from .db import init_db

log = logging.getLogger("uvicorn")


def create_application() -> FastAPI:
    application = FastAPI()

    application.include_router(ping.router)
    application.include_router(
        summaries.router, prefix="/summaries", tags=["summaries"]
    )
    return application


app = create_application()


@app.on_event("startup")
async def startup_event():
    log.info("Starting up...")
    init_db(app)


@app.on_event("shutdown")
async def shutdown_event():
    log.info("Shutting down...")


@app.get("/")
async def root():
    """docstring"""
    return {"message": "Hello world!"}


@app.get("/ping")
async def pong(settings: Settings = Depends(get_settings)):
    """docstring"""
    return {
        "ping": "pong",
        "environment": settings.environment,
        "testing": settings.testing,
    }
