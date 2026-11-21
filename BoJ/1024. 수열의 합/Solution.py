# N = (start + start + length - 1) / 2 * length
# N * 2 / length - length + 1 = 2 * start (even int)

n, l = map(int, input().split())

def arr(n, l):
    for length in range(l, 101):
        start = (2 * n / length) - length + 1
        start = start / 2
        if start > 0 and start == int(start):
            start = int(start)
            return ' '.join(map(str, list(range(start, start + length))))
    return -1

print(arr(n, l))