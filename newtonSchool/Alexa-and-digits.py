# Your code here
n = int(input())
print("Yes" if any(n%i==0 and 1<=n//i<=9 for i in range(1,10)) else "No")