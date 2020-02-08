import datetime
def label_dow(Data):
    map = []
    tot_classes = 7
    for row in Data:
        date = row.split('/')
        date = datetime.date.fromisoformat(date[2]+'-'+date[0]+'-'+date[1])
        map.append(date.weekday())
    return tot_classes, map

def label_pair(Data):
    destinations = {}
    destinations['The Palace Of Fine Arts, 3601 Lyon St, San Francisco, CA'] = 0
    destinations['Embarcadero, San Francisco, CA'] = 1  
