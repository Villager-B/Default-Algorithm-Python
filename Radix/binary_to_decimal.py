def main():
    n = input("binary number : ")
    result = 0
    n = n[::-1]
    for i in range(len(n)):
        result += int(n[i]) * (2 ** i)
    print("decimal : ", result)


if __name__ == '__main__':
    main()
