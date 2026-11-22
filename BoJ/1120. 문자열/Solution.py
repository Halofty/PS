import sys

a, b = sys.stdin.read().split()

def check_sl_words(a, b):
    length = len(a)
    cnt = 0
    for i in range(length):
        if a[i] != b[i]:
            cnt += 1
    return cnt

iter = len(b) - len(a) + 1
gap = 51
for i in range(iter):
    gap = min(gap, check_sl_words(a, b[i:]))

print(gap)