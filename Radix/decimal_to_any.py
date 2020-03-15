def main():
    n = int(input("number : "))
    base = int(input("base : "))

    print(any_convert(n, base))


def any_convert(n, base):
    result = ""

    while n > 0:
        result = str(n % base) + result
        n //= 2

    return result


if __name__ == '__main__':
    main()
