import math


def main():
    print(prime_detect(200))


def prime_detect(n):
    if n <= 1:
        return []
    prime = [2]
    lim = int(math.sqrt(n))

    data = [i + 1 for i in range(2, n, 2)]
    while lim > data[0]:
        prime.append(data[0])
        data = [j for j in data if j % data[0] != 0]

    return prime + data


if __name__ == '__main__':
    main()
