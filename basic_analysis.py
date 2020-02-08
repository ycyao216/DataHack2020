from dataParser import *
from label_funcs import *

parsed_data = csvReader('barts_hotspots.csv')
tot_classes,map = label_dow(parsed_data)