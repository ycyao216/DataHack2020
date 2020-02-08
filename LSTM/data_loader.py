import numpy as np
from ..dataParser import *
from random import randint
class data_loader():
    def __init__(file_name, path, jump=3, cutoff_percent=80, batch_size=20, days=10):
        self.jump = jump
        self.cutoff_percent = cutoff_precent
        self.batch_size = batch_size
        self.data_network = transNetwork(file_name)
        self.data_network.groupByConnection()
        self.path = path
        self.max_index = (len(self.data_network.avgPaths[path]))*cutoff_percent/100
        self.positions = max_index/jump
        self.days = days
        self.rows = self.data_network.avgPaths[path]

    def next_batch():
        x = np.zeros((batch_size, self.days, 3))
        for i in range(batch_size):
            start_index = randint(0,positions)*jump+1
            for k in range(self.days):
                x[i,k,:] = self.rows[start_index+k][3:6]
            print(k)
            y[i] = self.rows[start_index+k][3]
        return x,y
