def main():

    depth_3(0)


def depth_3(pos):
    if len(tree[pos]) == 2:
        depth_3(tree[pos][0])
        print(pos, end=" ")
        depth_3(tree[pos][1])
    elif len(tree[pos]) == 1:
        depth_3(tree[pos][0])
        print(pos, end=" ")
    else:
        print(pos, end=" ")


if __name__ == '__main__':
    tree = [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12],
            [13, 14], [], [], [], [], [], [], [], []]
    main()
