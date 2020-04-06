def main():
    print(calc("4 6 2 + * 3 1 - 5 * -"))


def calc(expression):
    stack = []
    for i in expression.split(" "):
        print(stack)
        if i == "+":
            b, a = stack.pop(), stack.pop()
            stack.append(a + b)
        elif i == "-":
            b, a = stack.pop(), stack.pop()
            stack.append(a - b)
        elif i == "*":
            b, a = stack.pop(), stack.pop()
            stack.append(a * b)
        elif i == "/":
            b, a = stack.pop(), stack.pop()
            stack.append(a // b)
        else:
            stack.append(int(i))
    return stack[0]


if __name__ == '__main__':
    main()
