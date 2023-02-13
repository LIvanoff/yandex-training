import re


def task1():

    with open("input.txt") as f:
        s = f.read()

    s = s.replace('\n', '')
    s = s.replace(' ', '')

    chars = dict.fromkeys(s, 0)
    for c in s:
        chars[c] += 1

    chars = dict(sorted(chars.items()))

    maxCount = max(chars.values())

    inStr = ''

    for i in range(maxCount + 1):
        for keys in chars.keys():
            if i < maxCount:
                if i < maxCount - chars[keys]:
                    inStr += ' '
                else:
                    inStr += '#'
            else:
                inStr += str(keys)

        inStr += '\n'
    print(inStr)

task1()
