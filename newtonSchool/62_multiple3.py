# Your code here
def helper(N: int) -> int:
    if N % 3 == 0:
        return 0
    digit = [0 for i in range(10)]
    sum = 0
    temp = N
    while N > 0:
        sum += N % 10
        digit[N % 10] += 1
        N = N // 10
    for i in range(3):
        val = sum - (sum // 3) * 3 + 3 * i
        if val > 0 and val < 10 and digit[val] > 0:
            return 1
    return 2 if temp > 100 else -1
n=int(input())
print(helper(n))
