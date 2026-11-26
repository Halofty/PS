import sys


data = sys.stdin.buffer.read().split()
n, m = int(data[0]), int(data[1])
# 각 노드는 dict: {문자(byte) -> 자식 dict}
root = {}
for i in range(2, 2 + n):
    cur = root
    for ch in data[i]:
        nxt = cur.get(ch)
        if nxt is None:
            nxt = {}
            cur[ch] = nxt
        cur = nxt

ans = 0
for i in range(2 + n, 2 + n + m):
    cur = root
    for ch in data[i]:
        cur = cur.get(ch)
        if cur is None:
            break
    else:
        ans += 1  # 끝까지 따라감 => S의 어떤 문자열의 접두사

print(ans)

