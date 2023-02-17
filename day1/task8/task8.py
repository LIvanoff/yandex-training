
def task8():
    with open("input.txt") as coord_file:
        line_list = coord_file.readlines()

    line_list = list(map(lambda it: it.replace("\n", ""), line_list))
    coords_array = list(map(lambda it: it.split(), line_list))

    for coord_id in range(len(coords_array)):
        coords_array[coord_id] = list(map(int, coords_array[coord_id]))
    coords_array.pop(0)
    row0 = list([row[0] for row in coords_array])
    row1 = list([row[1] for row in coords_array])

    print(str(min(row0)) + " " + str(min(row1)) + " " + str(max(row0)) + " " + str(max(row1)))

task8()
