def main():
    year_list = list(range(1950, 2051, 2))
    # print(year_list)

    for year in year_list:
        if (year % 100 == 0) and (year % 400 != 0):
            continue
        elif year % 4 == 0:
            print(year, end=" ")


if __name__ == '__main__':
    main()
