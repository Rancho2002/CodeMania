n = int(input())
x, y = 0, 0
mp = {}
for i in range(n-1):
    x, y = map(int, input().split())
    mp[x] = mp.get(x, 0) + 1
    mp[y] = mp.get(y, 0) + 1

for key, value in mp.items():
    if value == n-1:
        print("Yes")
        exit(0)
print("No")
# print(mp)