from fastapi import FastAPI
from pydantic import BaseModel
from typing import Union
from gini_coff import*
import asyncio

from typing import Dict
from uvicorn import Config, Server

class Item(BaseModel):
    poor: float
    midleclass: float
    rich: float
    poor_income: float
    midleclass_income: float
    rich_income: float

app = FastAPI()

@app.post("/items")
async def create_item(item: Item):
    result = ginicoff(item.poor, item.midleclass, item.rich, item.poor_income, item.midleclass_income, item.rich_income)
    return result

def start(app, host, port, loop = None):
    if loop is None:
        loop = asyncio.new_event_loop()
    port = port
    server_config = Config(app, host=host, port=port, loop=loop)
    server = Server(config=server_config)
    loop.create_task(server.serve())
    loop.run_forever()
start(app, 'localhost', 500)
