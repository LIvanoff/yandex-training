# unique_rows = sum(self.normal_matrix[0:])

def task9():
    with open("input.txt", 'r') as f:
        size = f.readline()
        size = list(map(int, size.split(' ')))
        array = ''
        for i in range(size[0]):
            array += f.readline()

        indexes = ''
        for i in range(size[2]):
            indexes += f.readline()

    array = list(map(int, array.split()))
    indexes = list(map(int, indexes.split()))

    matrix = [array[i:i + size[1]] for i in range(0, len(array), size[1])]
    coord = [indexes[i:i + 4] for i in range(0, len(indexes), 4)]
    print(coord)
    print(matrix)


task9()
