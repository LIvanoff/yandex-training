
def check_par(card1, card2):
    if card1 == 0 and card2 == 9:
        return 9, 0
    elif card1 == 9 and card2 == 0:
        return 0, 9
    else:
        return card1, card2


def task17():
    with open("input.txt", 'r') as f:
        first = f.readline()
        second = f.readline()

    first = first.replace(' \n', '')
    second = second.replace(' \n', '')

    first = list(map(int, first.split(' ')))
    second = list(map(int, second.split(' ')))

    count = 1
    while True:
        card_player1 = first[0]
        card_player2 = second[0]
        card_player1, card_player2 = check_par(card_player1, card_player2)

        if card_player1 > card_player2:
            first.append(first.pop(0))
            first.append(second.pop(0))
        elif card_player1 < card_player2:
            second.append(first.pop(0))
            second.append(second.pop(0))
        if len(second) < 1:
            print('first ' + str(count))
            break
        elif len(first) < 1:
            print('second ' + str(count))
            break
        if count == 1000000:
            print('botva')
            break
        count += 1


task17()
