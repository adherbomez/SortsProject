import math


def SetAverage(size, average, path):
    print('Average is completed for size '+ str(size))
    fileAverageBs = open(path, "a")
    summary = math.fsum(average) / 100
    fileAverageBs.write(str(size) + ": " + str(summary) + "\n")
