import sys

t = int(sys.stdin.readline())

def check(n):
    words = []
    for i in range(n):
        words.append(sys.stdin.readline().strip())
    for i in range(n):
        for j in range(n):
            if i != j:
                w = words[i] + words[j]
                if w == w[::-1]:
                    return w
    return 0

for _ in range(t):
    n = int(sys.stdin.readline())
    print(check(n))



