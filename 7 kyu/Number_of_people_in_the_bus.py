def number(bus_stops):
    num_people = 0
    for i in bus_stops:
        num_people = num_people + i[0] - i[1]
    return num_people
