from math import ceil
n, a, b = map(int, input().split())

def fight(n, a, b):
    cnt = 1
    while True:
        n = ceil(n/2)
        a = ceil(a/2)
        b = ceil(b/2)
            
        if a == b:
            return cnt
        
        cnt += 1

print(fight(n, a, b))