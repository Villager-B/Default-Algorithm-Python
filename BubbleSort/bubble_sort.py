def main():
    for i in range(len(data)):
        for j in range(len(data) - i - 1):
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]

    print(data)


if __name__ == '__main__':
    data = [6, 15, 4, 2, 8, 5, 11, 9, 7, 13]
    main()
