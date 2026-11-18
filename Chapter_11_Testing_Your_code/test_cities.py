#11-1 City, country

from city_functions import get_city_country

def test_city_country():
    """test unit for santiago chile"""
    formated_string = get_city_country('santiago','chile')
    assert formated_string == 'Santiago, Chile.'

def test_city_country2():
    """test unit for santiago chile and its population"""
    formated_string = get_city_country('santiago','chile', '5000000')
    assert formated_string == 'Santiago, Chile - population 5000000.'
