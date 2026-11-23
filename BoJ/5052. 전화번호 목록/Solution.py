import sys

t = int(sys.stdin.readline())
for _ in range(t):
    n = int(sys.stdin.readline())
    pnums = []
    consistency = True
    for i in range(n):
        pnums.append(sys.stdin.readline().strip())
    pnums.sort()
    for i in range(n-1):
        if pnums[i+1].startswith(pnums[i]):
            consistency = False
    print('YES' if consistency else 'NO')