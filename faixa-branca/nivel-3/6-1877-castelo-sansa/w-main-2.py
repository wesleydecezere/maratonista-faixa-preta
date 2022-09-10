n, k = input().split()
n = int(n)
k = int(k)

h = list(map(int, input().split()))

pico = 0

for i in range(1, n):
  if h[i] > h[i - 1] and h[i] > h[i + 1]:
    pico += 1

out = "beautiful" if pico == k else "ugly"

print(out)