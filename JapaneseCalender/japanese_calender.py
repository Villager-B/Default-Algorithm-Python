def main():
    year = int(input("year : "))
    print(change_jcalender(year))


def change_jcalender(wc):
    if wc < 1868:
        return "Not Supported"
    elif wc < 1912:
        return "明治" + str(wc - 1867) + "年"
    elif wc < 1926:
        return "大正" + str(wc - 1911) + "年"
    elif wc < 1989:
        return "昭和" + str(wc - 1925) + "年"
    elif wc < 2019:
        return "平成" + str(wc - 1988) + "年"
    else:
        return "令和" + str(wc - 2018) + "年"


if __name__ == '__main__':
    main()
