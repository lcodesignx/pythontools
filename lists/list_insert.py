#!/usr/local/bin/python3

countries = []
num_countries = int(input("How many countries have visited: "))
index = 0

print("Enter the names\n")
while (index < num_countries):
    country = input("Country: ")
    countries.insert(index, country)
    index += 1

print("\nCountries visited:")
for country in countries:
    print(country.title())
    

