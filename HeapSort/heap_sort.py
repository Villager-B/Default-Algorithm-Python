def main():
    # Generate Heap
    for i in range(len(data)):
        j = i
        while (j > 0) and (data[(j - 1) // 2] < data[j]):
            data[(j - 1) // 2], data[j] = data[j], data[(j - 1) // 2]
            j = (j - 1) // 2

    print(data)

    for i in range(len(data), 0, -1):
        data[i - 1], data[0] = data[0], data[i - 1]
        j = 0
        while ((2 * j + 1 < i - 1) and (data[j] < data[2 * j + 1])) \
                or ((2 * j + 2 < i - 1) and (data[j] < data[2 * j + 2])):

            if (2 * j + 2 == i - 1) or (data[2 * j + 1] > data[2 * j + 2]):

                data[j], data[2 * j + 1] = data[2 * j + 1], data[j]
                j = 2 * j + 1
            else:
                data[j], data[2 * j + 2] = data[2 * j + 2], data[j]
                j = 2 * j + 2

    print(data)


if __name__ == '__main__':
    data = [6, 15, 4, 2, 8, 5, 11, 9, 7, 13]
    main()
