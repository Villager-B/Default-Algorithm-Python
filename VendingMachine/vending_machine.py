import sys


def main():
    insert_price = input("insert : ")
    if not insert_price.isdecimal():
        print("整数を入力してください")
        sys.exit()

    product_price = input("product : ")
    if not product_price.isdecimal():
        print("整数を入力してください")
        sys.exit()

    change = int(insert_price) - int(product_price)

    if change < 0:
        print("お金が不足")
        sys.exit()

    # print("change : ", change)
    change_list = ["10000", "5000", "1000", "500", "100", "50", "10", "5", "1"]

    for cl in change_list:
        print(cl + "yen", ":", change // int(cl))
        change = change % int(cl)


if __name__ == '__main__':
    main()
