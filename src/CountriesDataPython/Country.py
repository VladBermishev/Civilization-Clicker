import CoordinatesGetter


class Country:

    def __init__(self, _name: str, _area: int, _population: int, _longitude=0, _latitude=0):
        self.name = _name
        self.area = _area
        self.population = _population
        if _latitude == 0 or _latitude == 0:
            coordinatesGetter = CoordinatesGetter.CoordinatesGetter()
            _longitude, _latitude = coordinatesGetter.GetCoordinates(self.name)
        self.longitude = _longitude
        self.latitude = _latitude

    def __CountGoldPrice(self, f):
        self.__goldPrice = f(self)

    def __CountWarriors(self, f):
        self.__warrriors = f(self)

    def __CountCapacity(self, f):
        self.__capacity = f(self)

    def GetGold(self):
        return self.__goldPrice

    def GetWarriors(self):
        return self.__warrriors

    def GetCapacity(self):
        return self.__capacity

    def ProcessPrices(self, goldFunc, warriorFunc, capacityFunc):
        self.__CountGoldPrice(goldFunc)
        self.__CountWarriors(warriorFunc)
        self.__CountCapacity(capacityFunc)

