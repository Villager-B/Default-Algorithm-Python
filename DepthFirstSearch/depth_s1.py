def main():

    depth_1(0)


def depth_1(pos):
    print(pos, end=" ")
    for i in tree[pos]:
        depth_1(i)


if __name__ == '__main__':
    tree = [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12],
            [13, 14], [], [], [], [], [], [], [], []]
    main()
