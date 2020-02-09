from dataParser import *
from label_funcs import *
from analysis_funcs import *
#import numpy as np

parsed_data, df = csvReader('barts_hotspots_sorted.csv')
tot_classes,map = label_dow(parsed_data)
sorted_data = class_sort(parsed_data, tot_classes, map)
max_length = 0
for i in range(tot_classes):
    max_length = max(max_length, len(sorted_data[i]))
numpy_data = np.zeros((max_length,tot_classes))
for i in range(tot_classes):
    numpy_data[0:len(sorted_data[i]),i] = np.asarray(sorted_data[i])
    np.savetxt('./analysis/by_dow.csv',numpy_data,delimiter=',')
