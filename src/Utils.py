def GetLinesFromFile(path):
    f = open(path, "r")
    return f.readLines()

def GetStringFromFile(path):
    f = open(path, "r")
    return f.read()
