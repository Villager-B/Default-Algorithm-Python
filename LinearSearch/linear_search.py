"""40を見つける"""


def main():
    d = [50, 30, 90, 10, 20, 70, 40, 80]
    found = False
    for i in range(len(d)):
        if d[i] == 40:
            print("Found ", i)
            foud = True
            break

    if not found:
        print("404")


if __name__ == '__main__':
    main()
