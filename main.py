import os
import sys

sys.path.append('/src')
from src import Utils
from src import Solver

Starting = "Finland"
Countries = ["Romania", "Algeria", "Fiji", "US Virgin Islands", "Turkey"]


AllCountries = Utils.GetCountryIDS()
AllDistances = Utils.GetDistancesGraph()


Route = Solver.Exec(Starting, Countries, AllCountries, AllDistances)
print(Route)


