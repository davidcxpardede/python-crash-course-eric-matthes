'''
Write a function that stores information about a car in a dictionary. The function should always receive a manufacturer and a model name. It should then accept an arbitrary number of keyword arguments. Call the function with the required information and two other name-value pairs, such as a color or an optional feature. Your function should work for a call like this one:
car = make_car('subaru', 'outback', color="blue", tow_package=True)
Print a dictionary that's returned to make sure all the information was stored correctly.
'''

def order_motorcycle(brand, model, **motorcycles_info):
    """Store and display information about motorcycles."""
    motorcycles_info['brand'] = brand
    motorcycles_info['model'] = model
    return motorcycles_info

motorcycle = order_motorcycle('Suzuki', 'GSX R-150', color='black', assurance=True)
print(motorcycle)
    
    