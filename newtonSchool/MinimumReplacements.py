s = input()
t = input()
ans = float("inf")

for i in range(len(s) - len(t) + 1):
    cnt = 0
    for j in range(len(t)):
        if t[j] != s[i + j]:
            cnt += 1
    ans = min(ans, cnt)

print(ans)