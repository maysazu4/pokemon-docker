import requests
def get_pokemon_attributes(pokemon_name):
   url= 'https://pokeapi.co/api/v2/pokemon/' + pokemon_name
   response = requests.get(url).json()
   pokemon = {'name' :  response['name'],
              'height': response['height'],
              'weight': response['weight'],
              'id': response['id'],
              'abilities':response['abilities']
              }
   return pokemon