from fastapi import APIRouter, HTTPException,Request
from starlette.responses import HTMLResponse
from starlette.templating import Jinja2Templates
from utils import utils

router = APIRouter()
templates = Jinja2Templates(directory="templates")


@router.get('/pokemons/{pokemon_name}', response_class=HTMLResponse)
def get_pokemon(request: Request,pokemon_name: str):
   pokemon = utils.get_pokemon_attributes(pokemon_name)
   return templates.TemplateResponse("pokemon.html", {"request": request, "attributes": pokemon})

  



