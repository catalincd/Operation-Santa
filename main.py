import sys
import time
from src import Wrapper
from src import Utils
start_time = time.time()




'''
adaugati in Countries si Starting ce vreti voi
daca vreti toate tarile:

Countries = [x for x in Utils.GetCountryIDS().keys() if x != Starting]
'''


Starting = "Kiribati"
Countries = ['Solomon Islands', 'Northern Mariana Islands', 'Laos', 'Thailand', 'Afghanistan', 'Mauritius', 'Rwanda', 'Georgia', 'Angola', 'Guinea-Bissau', 'The Gambia', 'Dominican Republic', 'Turks and Caicos Islands', 'El Salvador', 'Panama']
Countries = [x for x in Utils.GetCountryIDS().keys() if x != Starting]


Result = Wrapper.Exec(Starting, Countries)


print('\n Route:')
print(Result[0])
print('\n Current KM Done:')
print(Result[1])
print('\n Current Gifts:')
print(Result[2])
print('\n Timetable dict:')
print(Result[3])
print('\n KMH:')
print(Result[4])
print('\n GPH:')
print(Result[5])



print()
print()
print()
print("Finished in %s" % (time.time() - start_time))
