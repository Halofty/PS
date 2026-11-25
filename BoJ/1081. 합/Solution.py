# 0~9 = 45 = 45 * 1
# 00~99 = 45*10 + 45*10 = 45 * 20
# 000~999 = 45*20*10 + 45*100 = 45 * 300

# 0~22 = 45 + 45 + 10 * (0 + 1) + 2 * (3) + (1 + 2)

# ...

lower, upper = map(int, input().split())

def sum_digit(n):
    if n < 0:
        return 0
    total = 0
    w = 0
    low = 0
    while n:
        now = n%10
        p = 10 ** w
        n = n//10

        total += n * 45 * p
        total += now * (now-1) // 2 * p
        total += now * (low+1)

        low += now * p
        w += 1
    return total

print(sum_digit(upper) - sum_digit(lower-1))