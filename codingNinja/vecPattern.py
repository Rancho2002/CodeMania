def numberPattern(n):
    p=1
    m=1
    ans=[]
    for i in range(n):
        temp=[]
        for _ in range(n-m-1,-1,-1):
            temp.append(-1)
        for k in range(i+1):
            p= p%10 if p%10!=0 else 1
            temp.append(p)
            p+=1
        m+=1
        ans.append(temp)
    return ans

numberPattern(7)
'''
def numberPattern(n):

    # Write your code Here.
    # Return a 2-d list of integers
    p=1
    m=1
    for i in range(n):
        for _ in range(n-m-1,-1,-1):
            print(" ",end="")
        for k in range(i+1):
            p= p%10 if p%10!=0 else 1
            print(p,end="")
            p+=1
        m+=1
        print()

numberPattern(7)
# numberPattern(4)

'''