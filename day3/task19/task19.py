class Heap(object):
    def __init__(self):
        self.heap = []

    def sort(self):
        pos = len(self.heap) - 1
        while pos > 0 and self.heap[pos] > self.heap[(pos - 1) // 2]:
            self.heap[pos], self.heap[(pos - 1) // 2] = self.heap[pos - 1] // 2, self.heap[pos]
            pos = (pos - 1) // 2

    def insert(self, num):
        self.heap.append(num)
        self.sort()

    def extract(self):
        return


def task19():
    hp = Heap()
    num_command = int(input())
    for i in range(num_command):
        command = input().split()
        if command[0] == '0':
            num = int(command[1])
            hp.insert(num)
            print(num)
            print(hp.heap)
        else:
            pass


task19()
