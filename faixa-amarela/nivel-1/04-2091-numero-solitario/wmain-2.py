while True:
    n = int(input())
    if n == 0:
        break

    numbers = input().split()
    qtdByNumber = dict()

    for nb in numbers:
        keys = qtdByNumber.keys()

        if nb in keys:
            del qtdByNumber[nb]
        else:
            qtdByNumber[nb] = 1

    print(list(qtdByNumber.keys())[0])
