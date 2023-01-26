# Your code here
def solve(n):
    x=[str(oct(i))[2:] for i in range(1,n+1)]
    y=[str(i) for i in range(1,n+1)]
    # print(x)
    # print(y)
    count=0
    for i in range (n):
        if '7' in x[i] or '7' in y[i]:
            continue 
        else:
            count+=1
    return count

n=int(input())
print(solve(n))
