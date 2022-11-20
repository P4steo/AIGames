def choose_vil_path(y, d, m):
    path = ""
    if [2020, 1, 1] <= [y, d, m] <= [2020, 31, 3]:
        path += "VIL_merc_2020_01-03"
    elif [2020, 1, 4] <= [y, d, m] <= [2020, 31, 5]:
        path += "VIL_merc_2020_04-06"
    elif [2020, 1, 7] <= [y, d, m] <= [2020, 31, 12]:
        path += "VIL_merc_2020_07-12"
    elif [2021, 1, 1] <= [y, d, m] <= [2021, 31, 5]:
        path += "VIL_merc_2021_01-06"
    elif [2021, 1, 7] <= [y, d, m] <= [2021, 31, 12]:
        path += "VIL_merc_2021_07-12"
    else:
        path = ""
        # fix no data

    # generate whole path template "folder/convert_date_to_vil_file_name(datetime)"
    return "/content/drive/MyDrive/AiGames/" + path


def path_vil(data_observation):
    with open(data_observation, 'r') as file:
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
            print(k)
            y = int(k.split("-")[0])
            d = int(k.split("-")[2])
            m = int(k.split("-")[1])
            print(choose_vil_path(y, d, m))


path_vil('datasets/train_observations.csv')
