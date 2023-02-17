class Queue(object):
    def __init__(self):
        self.queue = None

    def push(self, ch):
        self.queue.append(ch)

    def pop(self):
        if len(self.queue) != 0:
            return self.queue.pop(0)
        else:
            return 'error'

    def front(self):
        if len(self.queue) != 0:
            return self.queue[0]
        else:
            return 'error'

    def size(self):
        return len(self.queue)

    def clear(self):
        self.queue.clear()
        return 0


if __name__ == '__main__':
    queue = Queue()
    command = input().split()
    queue.queue = []

    while True:
        if command[0] == 'push':
            queue.push(command[1])
            print('ok')

        elif command[0] == 'size':
            print(queue.size())

        elif command[0] == 'pop':
            if queue.front() != 'error':
                print(queue.pop())
            else:
                print('error')

        elif command[0] == 'clear':
            if queue.clear() == 0:
                print('ok')
            else:
                print('error')

        elif command[0] == 'front':
            if queue.front() != 'error':
                print(queue.front())
            else:
                print('error')

        elif command[0] == 'exit':
            print('bye')
            break

        command = input().split()
