meals = ("yoghurt", "roll", "steak",)
print(meals[0])

my_first_emoty_dictionary = {}
my_second_empty_dictionary = dict()

meals ={"breakfast":"yoghurt", "lunch":"roll", "dinner":"steak"}

print(meals)  

things = {1:"2", "steve": [1, 2, 3]}
print(things)
print(meals["breakfast"])

print(things["steve"][0])

print("breakfast" in meals)
print("supper" in meals)

meals["supper"]="pancakes" # this adds an entry, unless it's alread there in which case it updates it
print(meals)

del(meals["breakfast"])
print(meals)


print(list(meals))
print(meals.keys())

print(meals.values())

valuesList= meals.values()
print(valuesList)

# nesting dictionaries

countries ={
    "uk":{ "capital":"london", "population":1000},
    "germany": {"capital": "berlin", "population": 5000}
    
    }
print(countries)

print(countries["germany"]["population"])