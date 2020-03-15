def main():
    data = [10, 20, 30, 40, 50, 60, 70, 80, 90]
    print(binary_search(data, 90))


def binary_search(d, val):
    left = 0
    right = len(d) - 1
    while left <= right:
        mid = (left + right) // 2
        if d[mid] == val:
            return mid
        elif d[mid] < val:
            left = mid + 1
        else:
            right = mid - 1
    return -1


if __name__ == '__main__':
    main()
