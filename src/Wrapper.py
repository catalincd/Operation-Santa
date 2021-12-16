from src import Solver
from src import Utils

def Exec(Starting, Countries, BatchSize = 12, GiftsDistanceRatio = 0.7):

    AllCountries = Utils.GetCountryIDS()
    AllDistances = Utils.GetDistancesGraph()
    AllTimezones = Utils.GetTimeZones()
    AllChildren = Utils.GetChildren()

    Distance = 0
    Route = [Starting]
    Countries.sort(key=lambda x: AllTimezones[x])

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

            Starting = CurrentRoute[1][-1]
            if len(Countries) == 0:
                break

    Distances = [0]

    for i in range(1, len(Route)):
        first = AllCountries[Route[i - 1]]
        second = AllCountries[Route[i]]
        Distances.append(AllDistances[first][second] + Distances[i - 1])


    TimezoneCountries = Route.copy()
    TimezoneArray = []
    CurrentTimeZone = AllTimezones[TimezoneCountries[0]]

    ALL_KM = 0
    ALL_GIFTS = 0

    Timetable = {}
    CurrentTime = -2

    while len(TimezoneCountries) > 0:
        while AllTimezones[TimezoneCountries[0]] == CurrentTimeZone:
            TimezoneArray.append(TimezoneCountries[0])
            TimezoneCountries = TimezoneCountries[1::]

            if len(TimezoneCountries) == 0:
                break

        KM = 0
        GIFTS = 0

        for i in TimezoneArray:
            if i != "END":
                GIFTS += AllChildren[i]

        for i in range(0, len(TimezoneArray) - 1):
            KM += AllDistances[AllCountries[TimezoneArray[i]]][AllCountries[TimezoneArray[i+1]]]

        if len(TimezoneCountries) > 0:
            KM += AllDistances[AllCountries[TimezoneArray[-1]]][AllCountries[TimezoneCountries[0]]]

        KMH = int(KM * (1.0 / GiftsDistanceRatio)) * 1.2
        GPH = int(GIFTS * (1.0 / (1.0 - GiftsDistanceRatio))) * 1.5


        for i in range(0, len(TimezoneArray)):

            CurrentTime += 0.02

            if int(CurrentTime) < AllTimezones[TimezoneArray[i]]:
                CurrentTime = AllTimezones[TimezoneArray[i]]


            if KMH > 0:
                if i < len(TimezoneArray) - 1:
                    CurrentTime += AllDistances[AllCountries[TimezoneArray[i]]][AllCountries[TimezoneArray[i + 1]]] / KMH
                elif len(TimezoneCountries) > 0:
                    CurrentTime += AllDistances[AllCountries[TimezoneArray[i]]][AllCountries[TimezoneCountries[0]]] / KMH

            if GPH > 0:
                CurrentTime += AllChildren[TimezoneArray[i]] / GPH

            hrs = int(CurrentTime)
            mins = int((CurrentTime - int(CurrentTime)) * 60)

            if hrs < 10:
                hrs = "0{}".format(hrs)
            if mins < 10:
                mins = "0{}".format(mins)

            Timetable[TimezoneArray[i]] = "{}:{}".format(hrs, mins)


        TimezoneArray.clear()

        if len(TimezoneCountries) == 0:
            break

        CurrentTimeZone = AllTimezones[TimezoneCountries[0]]





    AllGifts = []
    CurrentGifts = 0

    for i in range(len(Route)):

        if i < len(Route)-1 and Route[i] != "END":
            CurrentGifts += AllChildren[Route[i]]



        AllGifts.append(CurrentGifts)



    return (Route, Distances, AllGifts, Timetable, KMH, GPH)

