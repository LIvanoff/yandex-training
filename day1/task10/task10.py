

def task10():
    s = input()
    chars = dict.fromkeys(s, 0)
    for c in s:
        chars[c] += 1

    chars = dict(sorted(chars.items()))

    for keys in chars.keys():
        print(str(keys) + ': ' + str(chars[keys]))

task10()