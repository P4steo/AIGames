with open('../datasets/route_definitions.csv', 'r') as file:
    line = file.readline()
    lenline = len(line)
    data = []
    while lenline > 0:
        line = file.readline()
        lenline = len(line)
        data.append(line)
    waypoints = []
    waypoints_og = []
    licznik = 1
    for i in data:
        licznik += 1
        if len(i) > 0:
            waypoints_og = i.split("\"")
            waypoints.append(waypoints_og[1])
    for element in waypoints:
        print(element)
