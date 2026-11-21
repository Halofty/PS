import sys

words = sys.stdin.read().split()[1:]

root = {}

for word in words:
    node = root

    for ch in word:
        node = node.setdefault(ch, {})

def cnt_leaves(node):
    if not node:
        return 1
    return sum(cnt_leaves(child) for child in node.values())

print(cnt_leaves(root))