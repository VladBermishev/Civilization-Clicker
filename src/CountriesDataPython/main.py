import os
import sys

root_path = os.path.abspath(os.getcwd())
for (dirpath, dirnames, filenames) in os.walk(root_path):
    for filename in filenames:
        if filename.endswith('.py'):
            sys.path.append(filename)

import pandas as pd
import DataTransformer
from CountingFunctions import *


path_to_csv = os.path.abspath(os.getcwd() + '\\countries_cleaned.csv')
dataFrame = pd.read_csv(path_to_csv)
data_transformer = DataTransformer.DataTransformer(dataFrame)
data_transformer.processPrices(CountGoldPrice, CountWarriors, CountCapacity)
data_transformer.save_to_json("data.json")


