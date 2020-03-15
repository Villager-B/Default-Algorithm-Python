def main():
    decimal = int(input("decimal : "))
    result = ""

    while decimal > 0:
        result = str(decimal % 2) + result
        decimal //= 2

    print("binary : ", result)


if __name__ == '__main__':
    main()
