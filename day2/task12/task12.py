def pair(ch):
    if ch == ')':
        return '('
    elif ch == ']':
        return '['
    elif ch == '}':
        return '{'


def task12():
    with open("input.txt") as f:
        s = f.read()

    s = list(s)
    s = list(filter(lambda sym: sym != ' ' and sym != '\n', s))
    stack = []
    for ch in s:
        if ch == '(' or ch == '[' or ch == '{':
            stack.insert(len(stack), ch)
        elif ch == ')' or ch == ']' or ch == '}':
            if 0 == len(stack):
                print('no\n')
                return
            elif pair(ch) != stack[-1]:
                print('no\n')
                return
            else:
                stack.pop(len(stack) - 1)
    if len(stack) == 0:
        print('yes\n')
    else:
        print('no\n')



task12()
