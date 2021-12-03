import numpy as np
from src import Utils
from itertools import combinations

def TSP(Countries, AllDistances):
    n = len(Countries)
    C = [[np.inf for _ in range(n)] for __ in range(1 << n)]
    Origin = [[-1 for _ in range(n)] for __ in range(1 << n)]
    CountryList = [["-" for _ in range(n)] for __ in range(1 << n)]
    C[1][0] = 0 # {0} <-> 1
    for size in range(1, n):
        for S in combinations(range(1, n), size):
            S = (0,) + S
            k = sum([1 << i for i in S])
            for i in S:
                if i == 0: continue
                for j in S:
                    if j == i: continue
                    cur_index = k ^ (1 << i)
                    cur_sum = C[cur_index][j] + AllDistances[Countries[j]][Countries[i]]
                    if cur_sum < C[k][i]:
                        #do stuff add country to list
                        Origin[k][i] = (cur_index, j)
                        CountryList[k][i] = j
                        C[k][i] = cur_sum
    all_index = (1 << n) - 1
    return (min([(C[all_index][i] + AllDistances[Countries[0]][Countries[i]], i) for i in range(n)]), CountryList)


def Exec(Starting, Countries, AllCountries, AllDistances):

    Countries.insert(0, Starting)
    for i in range(0, len(Countries)):
        Countries[i] = AllCountries[Countries[i]]

    Result = TSP(Countries, AllDistances)


    NamedCountries = []
    for i in Result[1][-1]:
        if i == '-':
            continue
        NamedCountries.append(list(AllCountries.keys())[list(AllCountries.values()).index(i)])

    print(Result[1])

    return (Result[0], NamedCountries)