def interestingPattern(n):

    # Write your code Here.
    # Return a list of strings.
    ans=[]
    val=[]
    for i in range(1,n+1):
        temp=65+n-1

        for j in range(i):
            val.append(chr(temp))
            temp-=1
        val.reverse()
        ans.append("".join(val))
        val=[]
    return ans
    
print(interestingPattern(5))