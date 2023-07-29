from city_functions import city_country

def test_city_country():
    """Test the function city_country()"""
    formatted_city_country = city_country('medan', 'sumatra utara')
    assert formatted_city_country == 'Medan, Sumatra Utara'