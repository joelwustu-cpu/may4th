import random


characters = [
    "Jedi Knight",
    "Padawan",
    "Rebel Pilot",
    "Boba Fett",
    "Smuggler",
    "Clone Trooper",
    "Resistance Spy"
]

planets = [
    "Tatooine",
    "Hoth",
    "Endor",
    "Naboo",
    "Coruscant",
    "Dagobah",
    "Mustafar"
]

missions = [
    "rescue a captured droid",
    "crack a twi'lek",
    "escape an Imperial base",
    "protect a hidden Jedi temple",
    "deliver a secret message",
    "destroy a Sith weapon",
    "find a lost lightsaber",
]

enemies = [
    "Darth Vader",
    "a Sith Inquisitor",
    "stormtroopers",
    "bounty hunters",
    "a crime lord",
    "battle droids",
    "the First Order",

]

allies = [
    "R2-D2",
    "Chewbacca",
    "Ahsoka Tano",
    "Obi-Wan Kenobi",
    "Hera Syndulla",
    "a group of Ewoks",
    "a mysterious rebel informant"
]

ships = [
    "Millennium Falcon",
    "X-wing",
    "TIE fighter",
    "Naboo starfighter",
    "Razor Crest",
    "Jedi starfighter",
    "The Ghost",
    "ARC-170 Starfighter"
]


def generate_mission():
    character = random.choice(characters)
    planet = random.choice(planets)
    mission = random.choice(missions)
    enemy = random.choice(enemies)
    ally = random.choice(allies)
    ship = random.choice(ships)
    difficulty = random.randint(1, 10)

    print("\n==============================")
    print("   STAR WARS MISSION BRIEFING")
    print("==============================")
    print("Character:", character)
    print("Planet:", planet)
    print("Mission:", mission)
    print("Enemy:", enemy)
    print("Ally:", ally)
    print("Ship:", ship)
    print("Difficulty:", difficulty)

    print("\nBriefing:")
    print(f"A {character} must travel to {planet} aboard the {ship}.")
    print(f"With help from {ally}, they must {mission} before {enemy} stops them.")

    if difficulty <= 3:
        print("This should be an easy mission.")
    elif difficulty <= 7:
        print("This mission will be dangerous.")
    else:
        print("This mission is extremely risky. I have a bad feeling about this.")

    print("May the Force be with you.")


print("Welcome to the Star Wars Mission Generator!")

while True:
    choice = input("\nGenerate a new mission? yes/no: ").lower()

    if choice == "yes":
        generate_mission()
    elif choice == "no":
        print("Goodbye, young Jedi.")
        break
    else:
        print("Please type yes or no.")