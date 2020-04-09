import numpy as np
from random import randint
import sys

sys.path.append('..')
from dataParser import *
class data_loader():
    def __init__(self, file_name, path, jump=3, cutoff_percent=80, batch_size=20, days=10):
        self.jump = jump
        self.cutoff_percent = cutoff_percent
        self.batch_size = batch_size
        self.data_network = transNetwork(file_name)
        self.data_network.groupByConnection()
        self.path = path
        self.max_index = (len(self.data_network.avgPaths[path]))*cutoff_percent/100
        self.positions = self.max_index/jump
        self.days = days
        self.rows = self.data_network.avgPaths[path]

    def next_batch(self):
        x = np.zeros((self.batch_size, self.days, 3))
        y = np.zeros((self.batch_size))
        for i in range(self.batch_size):
            start_index = randint(0,self.positions)*self.jump+1
            for k in range(self.days):
                x[i,k,:] = self.rows[start_index+k][3:6]
            y[i] = self.rows[start_index+self.days][3]
        # Normalize with mean
        x[:, :, 0] /= 665.0
        x[:, :, 1] /= 491.7
        x[:, :, 2] /= 901.0
        y /= 665.0
        return x,y
