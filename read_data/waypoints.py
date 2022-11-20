with open('../datasets/route_definitions.csv', 'r') as file:
    line = file.readline().strip()
    lenline = len(line)
    data = []
    while lenline > 0:
        line = file.readline()
        lenline = len(line)
        data.append(line)

    waypoints = []  # added after split elements with waypoints
    waypoints_id = []  # added after split elements with id
    waypoints_og = []  # temporary array
    id_waypoints = {}  # dictionary with id:waypoints

    for i in data:
        if len(i) > 0:
            waypoints_og = i.split("\"")
            waypoints.append(waypoints_og[1])
            waypoints_id.append((waypoints_og[0].split(","))[0])

    for k in range(0, len(waypoints)):
        id_waypoints[waypoints_id[k]] = waypoints[k]

    for i in id_waypoints:
        print("{i}:{value}".format(i=i, value=id_waypoints[i]))
with open('waypoints.txt', 'w') as plik:
    for i in id_waypoints:
        plik.write("{i}:{value}".format(i=i, value=id_waypoints[i]))
        plik.write("\n")
plik.close()
file.close()
