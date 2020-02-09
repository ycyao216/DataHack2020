import pandas
import numpy as np


origin = "Origin Display Name"
dest = "Destination Display Name"
travTime = "Daily Mean Travel Time (Seconds)"
date = "Date"

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
        self.csv = csv
        self.df = pandas.read_csv(self.csv, header = 0)
        self.headers = list(self.df.columns)
        self.network = self.csvReader()
        #dict of unique connection nagems
        self.avgPaths = self.getAllPath()
        #dict {date: list of connections}
        self.dateGroups = self.organizeByDate()

    def csvReader(self):
        connectionList = []
        for ind in self.df.index:
            connectionList.append(connection(self.df[origin][ind], self.df[dest][ind], self.df[travTime][ind]))
        return connectionList

    def organizeByDate(self):
        #dict {data: list of connections}
        dates = dict()
        for ind in self.df.index:
            dateTime = self.df[date][ind]
            o = self.df[origin][ind]
            d = self.df[dest][ind]
            t = self.df[travTime][ind]
            if (dateTime not in dates):
                dates[dateTime] = []
                dates[dateTime].append(connection(o,d,t))
            else:
                dates[dateTime].append(connection(o,d,t))
        return dates

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
                if(cases == connections.path):
                    sum += connections.time
                    count += 1
            self.avgPaths[cases] = sum/count

    def groupByConnection(self):
        for cases in self.avgPaths:
            otherData = []
            for ind in self.df.index:
                rowData = []
                if (self.df[origin][ind] + "->" +self.df[dest][ind] == cases):
                    for heads in self.headers:
                        if heads != origin and heads != dest:
                            rowData.append(self.df[heads][ind])
                    otherData.append(rowData)
            self.avgPaths[cases] = otherData

#Testing
network = transNetwork("C:\\Users\\Yunchao Yao\\Documents\\College\\Dataheck\\DataHacks\\data\\barts_hotspots.csv")
network.calculateAverage()
print(network.avgPaths)
network.groupByConnection()
print(network.avgPaths)