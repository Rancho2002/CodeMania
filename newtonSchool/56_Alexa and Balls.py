a, b, c, d = map(int, input().split())
result = 0
red = 0
target = d

if b >= c * d:
    result = -1
else:
    while a > red * d:
        a = a + b
        red = red + c
        result += 1

print(result)
