import sys
from collections import deque

input = sys.stdin.readline
t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    q = deque((p, i) for i, p in enumerate(map(int, input().split())))
    cnt = 0
    while q:
        cur = q.popleft()
        if any(cur[0] < p for p, _ in q):
            q.append(cur)
        else:
            cnt += 1
            if cur[1] == m:
                print(cnt)
                break