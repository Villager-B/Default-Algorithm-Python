import math


def main():
    for i in range(200):
        if prime_detect(i):
            print(i, end=" ")


def prime_detect(n):
    if n <= 1:
        return False

    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False

    return True


if __name__ == '__main__':
    main()
