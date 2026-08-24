# Problem 11-1: City,Country

def city_country(city, country):
    res = f"{city.title()}, {country.title()}"
    return res

# Problem 11-2: Population

def city_country_population(city, country, population=''):
    if population:
        res = f"{city.title()}, {country.title()} - population {population}"
    else:
        res = f"{city.title()}, {country.title()}"
    return res