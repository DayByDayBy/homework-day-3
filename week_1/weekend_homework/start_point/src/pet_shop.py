# WRITE YOUR FUNCTIONS HERE


def get_pet_shop_name(shop):
    return shop["name"]

def get_total_cash(shop):
    return shop["admin"]["total_cash"]

def add_or_remove_cash(shop, transaction):
    shop["admin"]["total_cash"] -= transaction

def add_or_remove_cash(shop, transaction):
    shop["admin"]["total_cash"] += transaction

def get_pets_sold(sold):
    return sold["admin"]["pets_sold"]

def increase_pets_sold(sold, sale):
    sold["admin"]["pets_sold"] += sale

def get_stock_count(pets):
 return len(pets["pets"])

def get_pets_by_breed (pets, breed):
    pet_breeds = []
    for pet in pets["pets"]:
        if pet["breed"] == breed:
            pet_breeds.append(breed)
    return pet_breeds

def find_pet_by_name(pets, name):
    for pet in pets["pets"]:
        if pet["name"] == name:
            return pet

def remove_pet_by_name(shop, name):
    for pet in shop["pets"]:
        if pet["name"] == name:
            shop["pets"].remove(pet)

def add_pet_to_stock(shop, new_pet):
    shop["pets"].append(new_pet)

def get_customer_cash(customer):
    return customer["cash"]

def remove_customer_cash(customer, transaction):
    customer["cash"] -= transaction

def get_customer_pet_count(customer_pet_count):
    return len(customer_pet_count["pets"])

def add_pet_to_customer(customer_pet_list, new_pet):
    customer_pet_list["pets"].append(new_pet)


def customer_can_afford_pet(customer, new_pet):
    return True if customer["cash"] >= new_pet["price"] else False

def sell_pet_to_customer(shop, pet, customer):
    if pet in shop["pets"] and customer_can_afford_pet(customer, pet):
        increase_pets_sold(shop, 1)
        remove_customer_cash(customer, pet["price"])
        add_pet_to_customer(customer, pet)
        add_or_remove_cash(shop, pet["price"])



#####   alt that runs, with a shorter if:

# def sell_pet_to_customer(shop, pet, customer):
#     if pet and customer_can_afford_pet(customer, pet):  ## if pet - can also be 'if pet != None'
#         increase_pets_sold(shop, 1)
#         remove_customer_cash(customer, pet["price"])
#         add_pet_to_customer(customer, pet)
#         add_or_remove_cash(shop, pet["price"])


