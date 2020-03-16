def main():

    depth_2(0)


def depth_2(pos):
    for i in tree[pos]:
        depth_2(i)
    print(pos, end=" ")


if __name__ == '__main__':
    tree = [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12],
            [13, 14], [], [], [], [], [], [], [], []]
    main()
