from fastapi import FastAPI
from typing import Union
from pydantic import BaseModel
from routes.datos import appRouter

app = FastAPI()

app.include_router(appRouter)
