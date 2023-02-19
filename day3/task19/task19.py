class Heap(object):
    def __init__(self):
        self.heap = []
        self.max = 0

    def sort(self):
        pos = len(self.heap) - 1
        while pos > 0 and self.heap[pos] > self.heap[(pos - 1) // 2]:
            self.heap[pos], self.heap[(pos - 1) // 2] = self.heap[(pos - 1) // 2], self.heap[pos]
            pos = (pos - 1) // 2

    def insert(self, num):
        self.heap.append(num)
        self.sort()

    def extract_max(self):
        max = self.heap[0]
        self.heap[0] = self.heap[-1]
        pos = 0
        while pos * 2 + 2 < len(self.heap):
            min_son_index = pos * 2 + 1
            if self.heap[pos * 2 + 2] > self.heap[min_son_index]:
                min_son_index = pos * 2 + 2
            if self.heap[pos] < self.heap[min_son_index]:
                self.heap[pos], self.heap[min_son_index] = self.heap[min_son_index], self.heap[pos]
                pos = min_son_index
            else:
                break
        self.heap.pop()
        return max


def task19():
    hp = Heap()
    num_command = int(input())
    for i in range(num_command):
        command = input().split()
        if command[0] == '0':
            num = int(command[1])
            hp.insert(num)
        else:
            print(hp.extract_max())


task19()
