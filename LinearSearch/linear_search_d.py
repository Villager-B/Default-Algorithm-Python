def main():
    d = [50, 30, 90, 10, 20, 70, 40, 80]
    print(linear_search(d, 40))


def linear_search(list_data, search_number):
    for i in range(len(list_data)):
        if list_data[i] == search_number:
            return i
    return -1


if __name__ == '__main__':
    main()
