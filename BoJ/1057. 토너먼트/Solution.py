from math import ceil
n, a, b = map(int, input().split())

def fight(a, b):
    cnt = 1
    while True:
        a = ceil(a/2)
        b = ceil(b/2)
            
        if a == b:
            return cnt
        
        cnt += 1

print(fight(a, b))