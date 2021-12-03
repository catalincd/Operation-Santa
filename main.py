import os
import sys

sys.path.append('/src')
from src import Utils
from src import Solver

Starting = "Finland"
Countries = ["Romania", "Algeria", "Zimbabwe", "US Virgin Islands", "Fiji"]


AllCountries = Utils.GetCountryIDS()
AllDistances = Utils.GetDistancesGraph()


Route = Solver.Exec(Starting, Countries, AllCountries, AllDistances)
print(Route)


