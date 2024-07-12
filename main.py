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