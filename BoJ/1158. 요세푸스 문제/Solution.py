from collections import deque
import sys

n, k = map(int, sys.stdin.read().split())
k = -k + 1
queue = deque(list(range(1, n+1)))
ans = []

for i in range(n):
    queue.rotate(k)
    ans.append(queue.popleft()  )
print('<' + ', '.join(map(str, ans)) + '>')