def main():

    search([])


def diagonally_cheak(x, col):
    for i, row in enumerate(reversed(col)):
        # print(row)
        if (x + i + 1 == row) or (x - i - 1 == row):
            return False
    return True


def search(col):
    if len(col) == N:
        print(col)
        return

    for i in range(N):
        if i not in col:
            if diagonally_cheak(i, col):
                col.append(i)
                search(col)
                col.pop()


if __name__ == '__main__':
    N = 8
    main()
