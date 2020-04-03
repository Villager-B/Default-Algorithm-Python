import random


def main():
    play(0, 0, True)


def clear_cheak(player):
    for mask in goal:
        if player & mask == mask:
            return True
    return False


def minimax(p1, p2, turn):
    if clear_cheak(p2):
        if turn:
            return 1
        else:
            return -1

    board = p1 | p2
    if board == 0b111111111:
        return 0

    w = [i for i in range(9) if (board & (1 << i)) == 0]

    if turn:
        return min([minimax(p2, p1 | (1 << i), not turn) for i in w])
    else:
        return max([minimax(p2, p1 | (1 << i), not turn) for i in w])


def play(p1, p2, turn):
    if clear_cheak(p2):
        print([bin(p1), bin(p2)])
        return

    board = p1 | p2
    if board == 0b111111111:
        print("Draw")
        print([bin(p1), bin(p2)])
        return

    w = [i for i in range(9) if (board & (1 << i)) == 0]
    r = [minimax(p2, p1 | (1 << i), True) for i in w]
    i = [i for i, x in enumerate(r) if x == max(r)]
    j = w[random.choice(i)]
    play(p2, p1 | (1 << j), not turn)


if __name__ == '__main__':
    goal = [
        0b111000000, 0b000111000, 0b000000111, 0b100100100,
        0b010010010, 0b001001001, 0b100010001, 0b001010100
    ]
    main()
