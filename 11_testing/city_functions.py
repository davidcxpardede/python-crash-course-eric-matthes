def city_country(city, country, population=''):
    """Return a single string of the form City, Country."""
    if population:
        formatted_city_country = f"{city.title()}, {country.title()} - population {population} million"
    else:
        formatted_city_country = f"{city.title()}, {country.title()}"
    return formatted_city_country