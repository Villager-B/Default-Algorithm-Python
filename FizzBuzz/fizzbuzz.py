"""FizzBuzz
1-50までの数を出力する．なお，以下の条件を満たすこと
- 3の倍数：「Fizz」
- 5の倍数：「Buzz」
- 3,5の倍数：「FizzBuzz」
"""


def main():
    for i in range(1, 51):
        if i % 15 == 0:
            print("FizzBuzz", end=" ")
        elif i % 3 == 0:
            print("Fizz", end=" ")
        elif i % 5 == 0:
            print("Buzz", end=" ")
        else:
            print(i, end=" ")


if __name__ == '__main__':
    main()
