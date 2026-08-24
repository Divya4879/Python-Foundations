# Testing city_functions

from city_functions import city_country

def test_city_country():
    res = city_country('jaipur', 'india')
    assert res == 'Jaipur, India'   # == used- testing