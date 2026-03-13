import requests

country = input("Enter country: ")

url = f'https://restcountries.com/v3.1/name/{country}'
response = requests.get(url)

data = response.json()

all_countries_info = data[0]
name = all_countries_info['name']['common']
capital = all_countries_info['capital'][0]
region = all_countries_info['region']
population = all_countries_info['population']
languages = ', '.join(all_countries_info['languages'].values())

# Printing the extracted info
print(f"Capital: {capital}")
print(f"Region: {region}")
print(f"Population: {population}")
print(f"Languages: {languages}")

