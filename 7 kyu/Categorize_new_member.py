def open_or_senior(data):
    soo = []
    for i in data:
        if i[0] >= 55 and i[1] > 7:
            soo.append('Senior')
        else:
            soo.append('Open')
    return soo