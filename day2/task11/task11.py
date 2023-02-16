class Stack(object):
    def __init__(self):
        self.stack = None

    def push(self, ch):
        self.stack.insert(len(self.stack), ch)

    def pop(self):
        if len(self.stack) != 0:
            return self.stack.pop(len(self.stack) - 1)
        else:
            return 'error'

    def top(self):
        if len(self.stack) != 0:
            return self.stack[-1]
        else:
            return 'error'

    def size(self):
        return len(self.stack)

    def clear(self):
        self.stack.clear()
        return 0


if __name__ == '__main__':
    stack = Stack()
    command = input().split()
    stack.stack = []

    while True:
        if command[0] == 'push':
            stack.push(command[1])
            print('ok')

        elif command[0] == 'size':
            print(stack.size())

        elif command[0] == 'pop':
            if stack.top() != 'error':
                print(stack.pop())
            else:
                print('error')

        elif command[0] == 'clear':
            if stack.clear() == 0:
                print('ok')
            else:
                print('error')

        elif command[0] == 'back':
            if stack.top() != 'error':
                print(stack.top())
            else:
                print('error')

        elif command[0] == 'exit':
            print('bye')
            break

        command = input().split()
