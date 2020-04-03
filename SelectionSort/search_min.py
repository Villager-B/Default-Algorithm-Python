def main():
    min = data[0]
    for i in range(len(data)):
        if data[min] > data[i]:
            min = i

    print(min)


if __name__ == '__main__':
    data = [6, 15, 4, 2, 8, 5, 11, 9, 7, 13]
    main()
