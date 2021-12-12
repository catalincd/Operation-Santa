from src import Solver
from src import Utils

def Exec(Starting, Countries, BatchSize = 15, GiftsDistanceRatio = 0.2):

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

    while len(TimezoneCountries) > 0:
        while AllTimezones[TimezoneCountries[0]] == CurrentTimeZone:
            TimezoneArray.append(TimezoneCountries[0])
            TimezoneCountries = TimezoneCountries[1::]

            if len(TimezoneCountries) == 0:
                break

        KM = 0
        GIFTS = 0

        for i in TimezoneArray:
            GIFTS += AllChildren[i]

        for i in range(0, len(TimezoneArray) - 1):
            KM += AllDistances[AllCountries[TimezoneArray[i]]][AllCountries[TimezoneArray[i+1]]]

        if len(TimezoneCountries) > 0:
            KM += AllDistances[AllCountries[TimezoneArray[len(TimezoneArray) - 1]]][AllCountries[TimezoneCountries[0]]]

        ALL_KM = max(ALL_KM, KM)
        ALL_GIFTS = max(ALL_GIFTS, GIFTS)

        TimezoneArray.clear()

        if len(TimezoneCountries) == 0:
            break

        CurrentTimeZone = AllTimezones[TimezoneCountries[0]]

    AllGifts = []
    CurrentGifts = 0

    KMH = int(ALL_KM * (1.0 / GiftsDistanceRatio))
    GPH = int(ALL_GIFTS * (1.0  / (1.0 - GiftsDistanceRatio)))

    Timetable = {}
    CurrentTime = 0.0

    for i in range(len(Route)):

        if int(CurrentTime) < AllTimezones[Route[i]]:
            CurrentTime = AllTimezones[Route[i]]

        hrs = int(CurrentTime)
        mins = int((CurrentTime - int(CurrentTime)) * 60)

        if hrs < 10:
            hrs = "0{}".format(hrs)
        if mins < 10:
            mins = "0{}".format(mins)

        Timetable[Route[i]] = "{}:{}".format(hrs, mins)

        if i < len(Route)-1:
            CurrentTime += AllChildren[Route[i]] / GPH
            CurrentTime += AllDistances[AllCountries[Route[i]]][AllCountries[Route[i + 1]]] / KMH

        CurrentGifts += AllChildren[Route[i]]
        AllGifts.append(CurrentGifts)



    return (Route, Distances, AllGifts, Timetable, KMH, GPH)

