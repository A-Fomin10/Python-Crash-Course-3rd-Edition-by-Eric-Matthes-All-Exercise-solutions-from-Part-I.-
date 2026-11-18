#11-1 City, country

def get_city_country(city, country, population=''):
    """Function that gets a city and a country and returns a formatted 
    string. """
    city = city.title()
    country = country.title()
    if population:
        formated = f'{city}, {country} - population {population}.'
    else:
         formated = f'{city}, {country}.'
        
    print(formated)
    return formated

