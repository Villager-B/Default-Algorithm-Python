def main():
    print(gcd(1274, 975))


def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


if __name__ == '__main__':
    main()
