import requests
print("Welcome to the Python Pokédex!")
print("Search for Pokémon and view their information.")

def get_pokemon_data(pokemon_name):
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name.lower()}"
    response = requests.get(url)

    if response.status_code == 200:
        return response.json()
    else:
        return None
    
def display_pokemon(data):
    print("\n========================")
    print("      Pokémon Info")
    print("========================")

    print("Name:", data["name"].title())
    print("ID:", data["id"])
    print("Height:", data["height"])
    print("Weight:", data["weight"])

    print("\nTypes:")
    for type_info in data["types"]:
        print("-", type_info["type"]["name"].title())

    print("\nAbilities:")
    for ability_info in data["abilities"]:
        print("-", ability_info["ability"]["name"].title())

    print("\nBase Stats:")
    for stat_info in data["stats"]:
        stat_name = stat_info["stat"]["name"]
        stat_value = stat_info["base_stat"]
        print(f"- {stat_name.title()}: {stat_value}")
    print("\nstrongest Stats")
    strongest_stat = ""
    strongest_value = 0
    for stat_info in data["stats"]:
        stat_name = stat_info["stat"]["name"]
        stat_value = stat_info["base_stat"]
        if stat_value > strongest_value:
               strongest_value = stat_value
               strongest_stat = stat_name
    print("\nstrongest Stats")
while True:
    pokemon_name = input("\nEnter a Pokémon name or ID, or type 'quit': ").lower()

    if pokemon_name == "quit":
        print("bye")
        break

    data = get_pokemon_data(pokemon_name)

    if data:
        display_pokemon(data)
    else:
        print("Pokémon not found. Please try again.")
        
