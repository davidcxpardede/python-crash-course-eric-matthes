'''
Make a dictionary called cities. Use the name of three cities as keys in your dictionary. Create a dictionary of information about each city and include the country that the city is in, its approximate population, and one fact about that city. Print the name of each city and all of the information you have stored about it.
'''

cities = {
    'medan': {
        'province': 'North Sumatra',
        'pop': 2.4,
        'fact': 'Kota Ketua',},
    'bandung': {
        'province': 'West Java',
        'pop': 2.5,
        'fact': 'Paris van Java',},
    'surabaya': {
        'province': 'East Java',
        'pop': 3.1,
        'fact': 'Kota Pahlawan',}
    }

for city, info in cities.items():
    print(f"\n{city.title()} is located in {info['province']} and has a population of {info['pop']} million. It is known as {info['fact']}.")