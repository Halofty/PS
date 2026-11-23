import sys

t = int(sys.stdin.readline())
for _ in range(t):
    n, m = map(int,sys.stdin.readline().split())
    nums = list(map(int, sys.stdin.readline().split()))
    target = nums[m]
    # target이상: 먼저출력
    res = sum([1 if nums[i] > target else 0 for i in range(n)])
    stack = nums[m+1:] + nums[:m]
    # target보다 큰 값중 최솟값 : locmin
    locmin = 11
    for i in range(target+1, 10):
        if i in nums:
            locmin = i
            break

    while stack:
        num = stack.pop()
        if num == target:
            res+=1
        elif num == locmin:
            break
    print(res+1) # 본인까지 +1
    
    