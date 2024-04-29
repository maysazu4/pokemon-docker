from fastapi import FastAPI
from routes import pokemon_route


app = FastAPI()
app.include_router(pokemon_route.router)

