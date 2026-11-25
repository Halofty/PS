n, k = map(int, input().split())

total = n * k
m = min(n, k)
i = 1
while i <= m:
    q = k // i   # 몫
    j = min(k // q, m)  # 몫 같은 last i
    total -= q * (i + j) * (j - i + 1) // 2   # q × (i + … + j)
    i = j + 1
print(total)