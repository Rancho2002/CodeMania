def solve():
    input()
    sequence = set(map(int, input().split()))
    for i in range(2001):
        if i not in sequence:
            return i
print(solve())
