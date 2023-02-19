class Heap(object):
    def __init__(self):
        self.heap = None

    def extract_max(self, limit):
        max = self.heap[0]
        self.heap[0] = self.heap[limit]
        pos = 0
        while pos * 2 + 2 < limit + 1:  # len(self.heap):
            min_son_index = pos * 2 + 1
            if self.heap[pos * 2 + 2] > self.heap[min_son_index]:
                min_son_index = pos * 2 + 2
            if self.heap[pos] < self.heap[min_son_index]:
                self.heap[pos], self.heap[min_son_index] = self.heap[min_son_index], self.heap[pos]
                pos = min_son_index
            else:
                break
        self.heap[limit] = max

    def end_heapify(self, pos):
        limit = len(self.heap)
        min_son_index = pos * 2 + 1
        if self.heap[pos] < self.heap[pos * 2 + 1]:
            self.heap[pos], self.heap[pos * 2 + 1] = self.heap[pos * 2 + 1], self.heap[pos]
            pos = min_son_index

        while pos * 2 + 2 < limit:
            min_son_index = pos * 2 + 1
            max_son_index = min_son_index + 1
            if self.heap[max_son_index] > self.heap[min_son_index]:
                min_son_index = max_son_index
            if self.heap[pos] < self.heap[min_son_index]:
                self.heap[pos], self.heap[min_son_index] = self.heap[min_son_index], self.heap[pos]
                pos = min_son_index
            else:
                break

    def heapify(self, pos):
        while pos * 2 + 2 < len(self.heap):
            min_son_index = pos * 2 + 1
            if self.heap[pos * 2 + 2] > self.heap[min_son_index]:
                min_son_index = pos * 2 + 2
            if self.heap[pos] < self.heap[min_son_index]:
                self.heap[pos], self.heap[min_son_index] = self.heap[min_son_index], self.heap[pos]
                pos = min_son_index
            else:
                break

    def heapsort(self, array):
        self.heap = array
        limit = (len(self.heap) - 2) // 2
        if len(self.heap) % 2 == 0:
            self.end_heapify(limit)
        for pos in range(len(self.heap) - 1, -1, -1):
            self.heapify(pos)

        for i in range(len(self.heap)):
            self.extract_max(len(self.heap) - 1 - i)

        return self.heap


def task20():
    with open("input.txt", 'r') as f:
        num_command = f.readline()
        array = f.readline()

    array = list(map(int, array.split(' ')))
    hp = Heap()
    hp.heapsort(array)
    print(" ".join(map(str, hp.heap)))


task20()
