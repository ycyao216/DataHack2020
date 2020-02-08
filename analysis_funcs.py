def class_sort(Data, tot_classes, map):
    sorted_data = []
    target_column = 5
    for i in range(tot_classes):
        tmp = []
        sorted_data.append(tmp)
    for i in range(Data.shape[0]-1):
        if(Data[i+1,target_column]==''):
            print('Empty value, index '+i)
            continue
        sorted_data[map[i]].append(Data[i+1,target_column])
    return sorted_data
