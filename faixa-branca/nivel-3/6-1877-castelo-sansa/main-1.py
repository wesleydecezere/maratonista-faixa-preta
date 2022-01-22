n, k = input().split()
n = int(n)
k = int(k)

h = input().split()

pico = 0
vale = 0
grow = True

for i in range(n):
    if i > 0:
        if h[i] > h[i - 1]:
            if grow == False:
                vale += 1
                grow = True
        elif h[i] < h[i - 1]:
            if grow == True:
                pico += 1
                grow = False

if pico == k and grow == False:
    print('beautiful')
else:
    print('ugly')
