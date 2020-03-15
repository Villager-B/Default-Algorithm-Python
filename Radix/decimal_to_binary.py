def main():
    decimal = int(input("decimal : "))
    q_list = []

    while True:
        r = decimal // 2
        q = decimal % 2

        q_list.append(str(q))
        if r == 0:
            break

        decimal = r

    print("binary : ", "".join(q_list[::-1]))


if __name__ == '__main__':
    main()
