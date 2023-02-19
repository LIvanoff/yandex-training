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

    def heapify(self, pos):

        while pos * 2 + 1 < len(self.heap):
            min_son_index = pos * 2 + 1
            if pos * 2 + 2 < len(self.heap):
                if self.heap[pos * 2 + 2] > self.heap[min_son_index]:
                    min_son_index = pos * 2 + 2
                if self.heap[pos] < self.heap[min_son_index]:
                    self.heap[pos], self.heap[min_son_index] = self.heap[min_son_index], self.heap[pos]
                    pos = min_son_index
            elif pos * 2 + 1 < len(self.heap):
                if self.heap[pos] < self.heap[min_son_index]:
                    self.heap[pos], self.heap[min_son_index] = self.heap[min_son_index], self.heap[pos]
                    pos = min_son_index
            else:
                break

    def heapsort(self, array):
        self.heap = array
        limit = (len(self.heap) - 2) // 2
        for pos in range(limit, -1, -1):
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
