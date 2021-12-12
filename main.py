import sys
import time
from src import Wrapper
start_time = time.time()


Starting = "Kiribati"
Countries = ['Solomon Islands', 'Northern Mariana Islands', 'Laos', 'Thailand', 'Afghanistan', 'Mauritius', 'Rwanda', 'Georgia', 'Angola', 'Guinea-Bissau', 'The Gambia', 'Dominican Republic', 'Turks and Caicos Islands', 'El Salvador', 'Panama']


Result = Wrapper.Exec(Starting, Countries)


print('\n Route:')
print(Result[0])
print('\n Current KM Done:')
print(Result[1])
print('\n Current Gifts:')
print(Result[2])
print('\n Timetable dict:')
print(Result[3])


print()
print()
print()
print("Finished in %s" % (time.time() - start_time))
