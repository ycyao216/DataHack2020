import numpy as np
from ../dataParser import *
from random import randint
class data_loader():
    def __init__(file_name, path, jump=3, cutoff_percent=80, batch_size=20):
        self.jump = jump
        self.cutoff_percent = cutoff_precent
        self.batch_size = batch_size
        self.data_network = transNetwork(file_name)
        self.data_network.groupByConnection()
        self.max_index = (len(self.data_network.network))*cutoff_percent/100
        self.positions = max_index/jump

    def next_batch():
        start_index = randint(0,positions)*jump+1
        x = np.zeros((batch_size, 10, 3))
