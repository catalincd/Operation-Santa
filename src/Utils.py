import csv
import json

def GetLinesFromFile(path):
    f = open(path, "r")
    return f.readlines()

def GetStringFromFile(path):
    f = open(path, "r")
    return f.read()

def GetChildren():
    with open('copii_la_fiecare_tara.json', 'r') as file:
        dict = json.loads(file.read().rstrip())
        dict["END"] = 9999999999
        return dict

def GetTimeZones():#Thank you Iustin
    timezone = {}

    timezone["END"] = 99

    with open('country-capitals.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        ok = 0
        for l in csv_reader:
            timezone[l[0]] = int(-float(l[2]) // 15 + 12)
    return timezone

def GetCountryIDS():
    lines = GetLinesFromFile('country-capitals.csv')
    dict = {}

    dict["END"] = -1

    for i in range(0, len(lines)):
        comma = lines[i].find(',')
        dict[lines[i][:comma]] = i

    return dict

def ParseLine(line):
    items = []
    i = line.find(',')
    while i != -1:
        items.append(line[:i])
        line = line[i+1::]
        i = line.find(',')

    items.append(line)
    return items

def DistanceToInt(dist):
    return int(dist[:-1:])

def GetDistancesGraph():
    lines = GetLinesFromFile('distante.csv')
    distances = []

    lastCountry = ''

    for i in range(0, len(lines)):
        line = ParseLine(lines[i])

        if(line[0] != lastCountry):
            lastCountry = line[0]
            distances.append([])

        if (len(distances[-1]) == len(distances) - 1):
            distances[-1].append(0)

        distances[-1].append(DistanceToInt(line[2]))


    return distances

