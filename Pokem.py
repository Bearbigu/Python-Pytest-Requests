import requests
token = 'c49a25b3285317c4936a5761834bc450'

response_new_pokemon = requests.post('https://pokemonbattle.me:9104/pokemons', headers = {'Content-Type': 'application/json','trainer_token' : token},
                         json = {'name' : 'Сибирский зверь', 'photo' : 'https://dolnikov.ru/pokemons/albums/076.png'} )
print(response_new_pokemon.text)


response_change_name = requests.put('https://pokemonbattle.me:9104/pokemons', headers = {'Content-Type': 'application/json','trainer_token' : token},
                                    json = {'pokemon_id' : 5990, 'name' : 'Зверь'})
print(response_change_name.text)

response_add_pokebol = requests.post('https://pokemonbattle.me:9104/trainers/add_pokeball',headers = {'Content-Type': 'application/json','trainer_token' : token},
                                     json = {'pokemon_id' : 5990})
print(response_add_pokebol.text)

response_delete_pokemon = requests.post ('https://pokemonbattle.me:9104/pokemons/kill', headers = {'Content-Type': 'application/json','trainer_token' : token},
                                         json =  {'pokemon_id' : 5990} )
print(response_delete_pokemon.text)
