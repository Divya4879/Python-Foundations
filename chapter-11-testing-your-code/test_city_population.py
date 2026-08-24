from city_functions import city_country_population

def test_city_country_population():
    res1 = city_country_population('patna', 'india')
    assert res1 == 'Patna, India'

    res2 = city_country_population('patna', 'india', 34_000_909)
    assert res2 == 'Patna, India - population 34000909'

    res3 = city_country_population('santiago', 'chile', 8_000_000)
    assert res3 == 'Santiago, Chile - population 8000000'