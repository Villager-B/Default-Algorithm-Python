def main():
    text = list("MURABITOLEG")
    pattern = list("TOL")

    for i in range(len(text)):
        match = True
        for j in range(len(pattern)):
            if text[i + j] != pattern[j]:
                match = False
                break

        if match:
            print(i)
            break


if __name__ == '__main__':
    main()
