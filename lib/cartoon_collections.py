def roll_call_dwarves(dwarves):
    for i in range(len(dwarves)):
        print(f'{i + 1}. {dwarves[i]}')

def summon_captain_planet(planeteer_calls):
    return [f'{planeteer.title()}!' for planeteer in planeteer_calls]

def long_planeteer_calls(words):
    for word in words:
        if len(word) > 4:
            return True
    return False

cheeses = ["cheddar", "gouda", "thyme"]

def find_the_cheese(foods):
    for food in foods:
        if food in cheeses:
            return food
    return None
