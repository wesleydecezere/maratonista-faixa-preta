n = int(input())

for _ in range(n):
    nwords, nsentences = [int(x) for x in input().split()]
    # words = dict()
    keys = []
    values = []

    for _ in range(nwords):
        keys.append(input())
        values.append(input())
        # words[key] = value

    for _ in range(nsentences):
        sentence = input()

        for i in range(nwords):
            sentence = sentence.replace(keys[i], values[i])

        print(sentence)

    print()
