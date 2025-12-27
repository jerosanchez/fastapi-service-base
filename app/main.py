from fastapi import FastAPI

from app.core.config import config

app = FastAPI(title=config.app_name, debug=config.debug)

@app.get("/")
def read_root():
    return "It works!"
