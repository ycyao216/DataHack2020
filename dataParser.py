import pandas
import numpy as np

def csvReader(fileName):
    df = pandas.read_csv("./data/"+fileName)
    simpleArray = df.to_numpy()
    return simpleArray

