class Deque(object):
    def __init__(self):
        self.deque = None

    def push_front(self, ch):
        self.deque.insert(0, ch)

    def push_back(self, ch):
        self.deque.append(ch)

    def pop_front(self):
        if len(self.deque) != 0:
            return self.deque.pop(0)
        else:
            return 'error'

    def pop_back(self):
        if len(self.deque) != 0:
            return self.deque.pop(-1)
        else:
            return 'error'

    def front(self):
        if len(self.deque) != 0:
            return self.deque[0]
        else:
            return 'error'

    def back(self):
        if len(self.deque) != 0:
            return self.deque[len(self.deque)-1]
        else:
            return 'error'

    def size(self):
        return len(self.deque)

    def clear(self):
        self.deque.clear()
        return 0


if __name__ == '__main__':
    deque = Deque()
    command = input().split()
    deque.deque = []

    while True:
        if command[0] == 'push_back':
            deque.push_back(command[1])
            print('ok')

        elif command[0] == 'push_front':
            deque.push_front(command[1])
            print('ok')

        elif command[0] == 'size':
            print(deque.size())

        elif command[0] == 'pop_front':
            if deque.front() != 'error':
                print(deque.pop_front())
            else:
                print('error')

        elif command[0] == 'pop_back':
            if deque.front() != 'error':
                print(deque.pop_back())
            else:
                print('error')

        elif command[0] == 'clear':
            if deque.clear() == 0:
                print('ok')
            else:
                print('error')

        elif command[0] == 'front':
            if deque.front() != 'error':
                print(deque.front())
            else:
                print('error')

        elif command[0] == 'back':
            if deque.back() != 'error':
                print(deque.back())
            else:
                print('error')

        elif command[0] == 'exit':
            print('bye')
            break

        command = input().split()
