'''
Write a function called describe_city() that accepts the name of a city and its country. The function should print a simple sentence. Give the parameter for the country a default value. Call your function for three different cities, at least one of which is not in the default country.
'''

def describe_city(city, country='Indonesia'):
    """Display the country a city is in.

    Args:
        city (_type_): _description_
        country (str, optional): _description_. Defaults to 'Indonesia'.
    """
    
    print(f"{city.title()} is in {country.title()}.")

describe_city('Medan')
describe_city(city='Bandung')
describe_city('Albuquerque', 'United States')