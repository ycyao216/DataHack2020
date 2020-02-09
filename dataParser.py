import pandas
import numpy as np


origin = "Origin Display Name"
dest = "Destination Display Name"
travTime = "Daily Mean Travel Time (Seconds)"


def csvReader(fileName):
    df = pandas.read_csv("./data/"+fileName)
    simpleArray = df.to_numpy()
    return simpleArray, df

class connection:
    def __init__(self,origin, destination, time = 0):
        self.path = origin + "->" + destination
        self.time = time

class transNetwork:
    def __init__(self, csv):
        # list of connections
        self.network = self.csvReader(csv)
        #dict of unique connection nagems
        self.avgPaths = self.getAllPath(self)

    def csvReader(self, csv):
        connectionList = []
        df = pandas.read_csv(csv, header=0)
        for ind in df.index:
            connectionList.append(connection(df[origin][ind], df[dest][ind],df[travTime][ind]))
        return connectionList

    def connectSame(self, connect1, connect2):
        if (connect1.path == connect2.path):
            return True
        return False

    def getAllPath(self):
        paths = dict()
        for connects in self.network:
            paths[connects.path] = 0
        return paths

    def calculateAverage(self):
        for cases in self.avgPaths:
            sum = count = 0
            for connections in self.network:
                if(self.connectSame(self.avgPaths[cases],connections)):
                    sum += connections.time
                    count += 1
            self.avgPaths[cases] = sum/count
