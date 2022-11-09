# def greet(name, time_of_day):
#     return "what a lovely " + time_of_day + ", " + name
# greeting = greet("you magnificent bastard", "evening")
# print(greeting)

# # def greet():
# #     print ("Hey Hey")
# # greeting = greet()
# # print(greeting)


# name_1 = 'Gary'
# time_of_day_1 = 'afternoon'
# greeting = greet(name_1, time_of_day_1)
# print (greeting)

# name_2 = "Mr Marshall"
# time_of_day_2 = "evening"
# greeting = greet(name_2, time_of_day_2)
# print(greeting)

def greet():
    words = "hey"
    return words

def greet_2():
    words = "hey"
    return words
print(greet_2())





chickens = [
  { "name": "Margaret", "age": 2, "eggs": 0 },
  { "name": "Hetty", "age": 1, "eggs": 2 },
  { "name": "Henrietta", "age": 3, "eggs": 1 },
  { "name": "Audrey", "age": 2, "eggs": 0 },
  { "name": "Mabel", "age": 5, "eggs": 1 },
]

def count_eggs(list):

    total_eggs = 0

    for bird in list:
        total_eggs += bird["eggs"]
        bird["eggs"] = 0 # eggs have been collected
    return(f"{total_eggs} eggs collected")
print(count_eggs(chickens))
