'''
Write a function called city_country() that takes in the name of a city and its country. The function should return a string formatted like this:
"Santiago, Chile"
Call your function with at least three city-country pairs, and print the values that are returned.
'''

def capital_city(city, country):
    """Display the name of the capital cities of countries."""
    print(f"{city.title()}, {country.title()}")

capital_city('Jakarta', 'Indonesia')
capital_city('Washington D.C.', 'United States')
capital_city('Berlin', 'Germany')