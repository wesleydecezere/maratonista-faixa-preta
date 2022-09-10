while True:
    m = int(input())
    if m == 0:
        break
    
    s = input()
    lens = []
    
    for i in range(len(s)):
        for j in range(m, len(s)):
            sub = s[i:j]
            
            if len(set(sub)) > m:
                lens.append(len(sub) - 1)
                break

    # print(s, lens)
    print(max(lens))