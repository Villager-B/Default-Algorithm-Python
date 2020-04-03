import os


def main():
    queue = ["./"]

    while len(queue) > 0:
        dir = queue.pop()
        for i in os.listdir(dir):
            if i == "Radix":
                print(dir + i)
            if os.path.isdir(dir + i):
                if os.access(dir + i, os.R_OK):
                    queue.append(dir + i + "/")


if __name__ == '__main__':
    main()
