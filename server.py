import asyncio
from os import getenv
from typing import Dict
from os.path import exists
from fastapi import FastAPI
from uvicorn import Config, Server
from starlette.responses import JSONResponse, FileResponse

from schemas import *

class GeneratorRestAPI(FastAPI):
    services: Dict[str, str]
    
    def __init__(
            self, 
        ) -> None:
        super().__init__()
        
        # Register routes
        self.add_api_route("/", self.homepage_get, methods=["GET"])
        self.add_api_route("/img/{file_name}", self.image_get, methods=["GET"])
        
    async def homepage_get(self):
        return JSONResponse({'RestAPI': 'Image Generator',\
            'website': 'https://aaa.aaa.aaa/'}, status_code=200)

    async def image_get(self, file_name: str):
        '''Returns the image with the given id'''
        path = f'{self.images_path}/{file_name}'
        if not exists(path):
            return JSONResponse({"content": "Image not found"}, status_code=404)
        return FileResponse(path, media_type='image/jpg')
    
    def start(self, host, port, loop = None):
        if loop is None:
            loop = asyncio.new_event_loop()
        port = port
        server_config = Config(self, host=host, port=port, loop=loop)
        server = Server(config=server_config)
        loop.create_task(server.serve())
        loop.run_forever()

api = GeneratorRestAPI()
api.start('localhost', 8080)
