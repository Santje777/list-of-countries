"""a list of 3 countries I'd like to visit:"""

countries= ["France", "Germany", "Belgium"]
print(countries)
countries.pop(2)
print(countries)
countries.insert(0, "Spain")
print(countries)
print(len(countries))
countries.sort()
print(countries)

countries= ["France", "Germany", "Belgium"]

for country in countries:
    print(f"My number {countries.index(country)+1} choice is {country}")

"""a dictionary of 3 countries I’d like to visit as a key and their capital city as a value"""

countries= {"France":"Paris", "Germany":"Berlin", "Belgium":"Brussels"}
print(countries)
del countries["Belgium"]
print(countries)
countries["Spain"] = "Madrid"
print(countries)
print(countries["France"])
print(countries["Germany"])
print(countries["Spain"])

#looping through each key
for country in countries:
    capital = countries[country]
    print(f"The capital of {country} is {countries[country]}")

print("Countries I'd like to visit:")

#looping through each key-value pair
index = 0
for country, capital in countries.items():
    print(f"{index+1}. {country} (Capital city:{capital})")
    index = index + 1

"""Calculation of total of population from a list of dictionaries"""    

def calculate_total_population(populations_list):
  """Calculate total population of all countries from list"""
  total = 0
  for population in populations:
    total = total + int(population['population'])
    
  return total

def display_total_population(total):
  """Convert to million"""
  total_in_millions = (round(total/1000000))
  """Print sentence"""
  print(f"The total population: {total_in_millions} million people")

#Initial data set
populations = [
  { 'country': "France", "population": "60000000"},
  { 'country': "Spain", "population": "50000000"},
  { 'country': "USA", "population": "30000000"},
  { 'country': "Australia", "population": "25000000"},
  { 'country': "Canada", "population": "38000000"},
]

# Display the total population such as, the total population is 203 million people
total_population = calculate_total_population(populations)
display_total_population(total_population)

