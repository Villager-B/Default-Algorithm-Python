def main():
    # d = [i for i in range(15)]
    # print(d)
    tree = [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12],
            [13, 14], [], [], [], [], [], [], [], []]
    # print(tree)
    data = [0]
    while len(data) > 0:
        pos = data.pop(0)
        print(pos, end=" ")
        for i in tree[pos]:
            data.append(i)


if __name__ == '__main__':
    main()
