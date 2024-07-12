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