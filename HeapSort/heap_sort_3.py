import heapq


def main():
    print(heap_sort(data))


def heap_sort(ary):
    h = ary.copy()
    heapq.heapify(h)
    return [heapq.heappop(h) for _ in range(len(ary))]


if __name__ == '__main__':
    data = [6, 15, 4, 2, 8, 5, 11, 9, 7, 13]
    main()
