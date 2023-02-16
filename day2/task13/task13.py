
def task13():
    with open("input.txt") as f:
        s = f.read()

    s = list(s)
    s = list(filter(lambda sym: sym != ' ' and sym != '\n', s))
    stack = []
    for ch in s:
        if ch != '+' and ch != '-' and ch != '*' and ch != '/':
            stack.insert(len(stack), ch)
        elif ch == '+' or ch == '-' or ch == '*' or ch == '/':
            a: int = stack[len(stack) - 1]
            stack.pop(len(stack) - 1)
            b: int = stack[len(stack) - 1]
            stack.pop(len(stack) - 1)
            if ch == '*':  # *
                stack.insert(len(stack), int(b) * int(a))
            elif ch == '+':  # +
                stack.insert(len(stack), int(b) + int(a))
            elif ch == '-':  # -
                stack.insert(len(stack), int(b) - int(a))
            elif ch == '/':  # /
                stack.insert(len(stack), int(b) / int(a))
    print(stack[0])


task13()
