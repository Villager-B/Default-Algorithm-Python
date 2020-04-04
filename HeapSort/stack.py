def main():
    stack = []
    stack.append(5)
    stack.append(8)
    stack.append(2)

    while len(stack) > 0:
        print(stack.pop())


if __name__ == '__main__':
    main()
