def city_country(city, country):
    """Return a single string of the form City, Country."""
    formatted_city_country = f"{city.title()}, {country.title()}"
    return formatted_city_country

city_country('medan', 'north sumatra')