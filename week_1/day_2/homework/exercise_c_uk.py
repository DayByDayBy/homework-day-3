united_kingdom = [
  {
    "name": "Scotland",
    "population": 5295000,
    "capital": "Edinburgh"
  },
  {
    "name": "Wales",
    "population": 3063000,
    "capital": "Swansea"
  },
  {
    "name": "England",
    "population": 53010000,
    "capital": "London"
  }
]

# 1. Change the capital of Wales from `"Swansea"` to `"Cardiff"`.
united_kingdom [1]["capital"] = Cardiff
# 2. Create a dictionary for Northern Ireland and add it to the `united_kingdom` list (The capital is Belfast, and the population is 1,811,000).
united_kingdom.append({"name": "Northern_Ireland", "population": 81000, "capital": "Belfast"})
# 3. Use a loop to print the names of all the countries in the UK.
for country in united_kingdom:
  totaly_pop =+country["populartion"]
  print(total_pop)

print country name 

# 4. Use a loop to find the total population of the UK.
