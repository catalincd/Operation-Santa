import os
import sys
import time
import random

start_time = time.time()

sys.path.append('/src')
from src import Utils
from src import Solver

AllCountries = Utils.GetCountryIDS()
AllDistances = Utils.GetDistancesGraph()
AllTimezones = Utils.GetTimeZones()

BatchSize = 12          # Maybe change this in production
Starting = "Kiribati"   # Maybe change this in production
Countries = []          # Fill this in production

# Test filling 'Countries'
for t in random.sample([x for x in AllCountries.keys() if x != Starting], 230):
    Countries.append(t)
# End of Test filling, Don't touch anything beyond this

Distance = 0
Route = [Starting]
Countries.sort(key=lambda x: AllTimezones[x])

print(Countries)

CurrentTimeZone = 0
while len(Countries) > 0:
    CurrentTimeZone = AllTimezones[Countries[0]]
    while AllTimezones[Countries[0]] == CurrentTimeZone:
        CurrentBatch = []
        while len(CurrentBatch) < BatchSize and AllTimezones[Countries[0]] == CurrentTimeZone:
            CurrentBatch.append(Countries[0])
            Countries = Countries[1::]
            if len(Countries) == 0:
                break

        CurrentRoute = Solver.Exec(Starting, CurrentBatch, AllCountries, AllDistances)
        Route.extend(CurrentRoute[1][1::])
        Distance += CurrentRoute[0]
        Starting = CurrentRoute[1][-1]

        if len(Countries) == 0:
            break



    print("KM: %s" % Distance)
    print("RouteLen: %s" % (len(Route)))
    print("CountriesLen: %s" % (len(Countries)))
    print(Route)
    print()




print("Finished in %s" % (time.time() - start_time))
