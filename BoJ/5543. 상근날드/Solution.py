import sys

prices = list(map(int, sys.stdin.read().split()))

print(min(prices[:3]) + min(prices[3:]) - 50)