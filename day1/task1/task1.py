

def task1():

    with open("input.txt") as f:
        s = f.read()

    s = s.replace('\n', '').replace(' ', '')

    chars = dict.fromkeys(s, 0)
    for c in s:
        chars[c] += 1

    chars = dict(sorted(chars.items()))

    maxCount = max(chars.values())

    inStr = ''

    for i in range(maxCount):
        for keys in chars.keys():
            if i < maxCount - chars[keys]:
                inStr += ' '
            else:
                inStr += '#'
        inStr += '\n'

    for item in chars:
        inStr += item


    # inStr += ''.join(chars)
    print(inStr)

task1()