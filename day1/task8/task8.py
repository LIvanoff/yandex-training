import numpy as np


def task8():
    with open("input.txt") as coord_file:
        line_list = coord_file.readlines()

    line_list = list(map(lambda it: it.replace("\n", ""), line_list))
    coords_array = list(map(lambda it: it.split(), line_list))

    for coord_id in range(len(coords_array)):
        coords_array[coord_id] = list(map(int, coords_array[coord_id]))
    coords_array.pop(0)
    print(coords_array)
    a = np.array(coords_array)
    a = a[a[:, 0].argsort()]
    x0 = a[0][0]
    x1 = a[len(a)-1][0]
    a = a[a[:, 1].argsort()]
    y0 = a[0][1]
    y1 = a[len(a) - 1][1]
    print(str(x0) + " " + str(y0) + " " + str(x1) + " " + str(y1))

task8()
