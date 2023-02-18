
class Heap(object):
    def __init__(self):
        self.heap = []

    def insert(self, num):
        self.heap.append(num)

    def extract(self):
        return


def task19():
    num_command = int(input())
    for i in range(num_command):
        command = input().split()
        if command[0] == '0':
            num = int(command[1])
            print(num)
        else:
            pass


task19()
