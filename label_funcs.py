import datetime
def label_dow(Data):
    map = []
    tot_classes = 7
    for i in range(1,Data.shape[0]):
        date = Data[i,0].split('/')
        if(len(date[0])==1):
            date[0] = '0'+date[0]
        if(len(date[1])==1):
            date[1] = '0'+date[1]
        date = datetime.date.fromisoformat(date[2]+'-'+date[0]+'-'+date[1])
        map.append(date.weekday())
    return tot_classes, map
