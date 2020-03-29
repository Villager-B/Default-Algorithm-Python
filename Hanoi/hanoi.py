def main():
    hanoi(n, "a", "b", "c")


def hanoi(n, src, dst, via):
    if n > 1:
        hanoi(n - 1, src, via, dst)
        print(src + " -> " + dst)
        hanoi(n - 1, via, dst, src)
    else:
        print(src + " -> " + dst)


if __name__ == '__main__':
    n = int(input())
    main()
