
def task14():
    with open("input.txt") as f:
        s = f.read()

    s = list(filter(lambda sym: sym != ' ' and sym != '\n', s))
    first_railway = list(map(int, s))
    first_railway.pop(0)
    dead_stack = []
    second_railway = []

    while len(first_railway) > 0:
        tmp = first_railway[0]
        first_railway.pop(0)
        while len(dead_stack) > 0 and dead_stack[0] < tmp:
            second_railway.insert(len(second_railway), dead_stack[0])
            dead_stack.pop(0)
        dead_stack.insert(0, tmp)

    while len(dead_stack) > 0:
        if len(second_railway) != 0:
            if dead_stack[0] < second_railway[-1]:
                print('NO')
                break
        second_railway.insert(len(second_railway), dead_stack[0])
        dead_stack.pop(0)
        if len(dead_stack) == 0:
            print('YES')
        print(second_railway)


task14()
