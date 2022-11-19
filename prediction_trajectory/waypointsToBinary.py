with open("../read_data/plik.txt", "r") as file:
    line = file.readline().strip()
    while (len(line) > 0):
        line = file.readline().strip()
        print(line)

