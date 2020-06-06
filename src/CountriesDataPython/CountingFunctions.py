import Country


def CountGoldPrice(country: Country.Country):
    return country.area + country.latitude + country.longitude + country.population


def CountWarriors(country: Country.Country):
    return country.area + country.latitude + country.longitude + country.population


def CountCapacity(country: Country.Country):
    return country.area + country.latitude + country.longitude + country.population
