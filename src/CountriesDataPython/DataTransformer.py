import pandas as pd
import json
import Country


class DataTransformer:

    def __init__(self, dataFrame: pd.DataFrame):
        self.countries = list()
        for index, row in dataFrame.iterrows():
            country = Country.Country(row["name"], row["area"], row["pop2005"], row["lon"], row["lat"])
            self.countries.append(country)

    def processPrices(self, goldPriceFunc, warriorsFunc, capacityFunc):
        for country in self.countries:
            country.ProcessPrices(goldPriceFunc, warriorsFunc, capacityFunc)

    def save_to_json(self,filename):
        countries = dict()
        for country in self.countries:
            countries[country.name] = [country.GetGold(), country.GetWarriors(), country.GetCapacity()]
        with open(filename, "w") as file_output:
            json.dump(countries, file_output)