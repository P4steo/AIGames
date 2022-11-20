def choose_vil_path(y, d, m):
    path = ""
    if [2020, 1, 1] <= [y, d, m] <= [2020, 3, 31]:
        path += "VIL_merc_2020_01-03"
    elif [2020, 4, 1] <= [y, d, m] <= [2020, 5, 31]:
        path += "VIL_merc_2020_04-06"
    elif [2020, 7, 1] <= [y, d, m] <= [2020, 12, 31]:
        path += "VIL_merc_2020_07-12"
    elif [2021, 1, 1] <= [y, d, m] <= [2021, 5, 31]:
        path += "VIL_merc_2021_01-06"
    elif [2021, 7, 1] <= [y, d, m] <= [2021, 12, 31]:
        path += "VIL_merc_2021_07-12"
    else:
        path = ""
        # fix no data

    # generate whole path template "folder/convert_date_to_vil_file_name(datetime)"
    return path


with open('datasets/train_observations.csv', 'r') as file:
    line = file.readline().strip()
    data = []
    while len(line) > 0:
        line = file.readline().strip()
        data.append(line)

    data_splited = []  # temporary array
    data_temp = []

    data_timestamp = []
    licznik = 0
    for i in data:
        licznik += 1
        if len(i) > 0:
            data_splited = i.split(",")
            data_timestamp.append(data_splited[2])

    for element in data_timestamp:
        data_temp.append(element.split(" ")[0])
    for k in data_temp:
        y = int(k.split("-")[0])
        d = int(k.split("-")[1])
        m = int(k.split("-")[2])
        print(choose_vil_path(y, d, m))
