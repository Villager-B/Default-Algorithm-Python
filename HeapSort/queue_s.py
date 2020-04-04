import queue


def main():
    q = queue.Queue()

    q.put(7)
    q.put(6)
    q.put(5)

    for i in range(3):
        print(q.get())


if __name__ == '__main__':
    main()
