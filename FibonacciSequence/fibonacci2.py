def main():
    print(fibonacci(7))
    print(memo)


def fibonacci(n):
    if n in memo:
        return memo[n]

    memo[n] = fibonacci(n - 1) + fibonacci(n - 2)

    return memo[n]


if __name__ == '__main__':
    memo = {1: 1, 2: 1}
    main()
