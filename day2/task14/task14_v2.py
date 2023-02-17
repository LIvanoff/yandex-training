def task14():
    with open("input.txt") as f:
        x = f.readline()  # число из первой строки
        line = f.readline()  # все остальные строки

    first_railway = list(map(int, line.split(' ')))
    dead_stack = []
    second_railway = []

    flag = True

    while len(first_railway) > 0:
        tmp = first_railway[0]
        first_railway.pop(0)
        while len(dead_stack) > 0 and dead_stack[0] < tmp:
            if len(second_railway) != 0:
                if dead_stack[0] < second_railway[-1]:
                    flag = False
                    print('NO')
                    break
            second_railway.insert(len(second_railway), dead_stack[0])
            dead_stack.pop(0)
        if not flag:
            break
        dead_stack.insert(0, tmp)

    while len(dead_stack) > 0 and flag:
        if len(second_railway) > 0:
            if dead_stack[0] < second_railway[-1]:
                print('NO')
                break
        second_railway.insert(len(second_railway), dead_stack[0])
        dead_stack.pop(0)
        if len(dead_stack) == 0:
            print('YES')

task14()
