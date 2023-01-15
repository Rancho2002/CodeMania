def isPalindrome(s,l,r):
    while(l<r):
        if(s[l]!=s[r]):
            return False
        l+=1
        r-=1
    return True

s=input()
n=len(s)
if(isPalindrome(s,0,n-1) and isPalindrome(s,0,(n-1)//2-1) and isPalindrome(s,(n+3)//2-1,n-1)):
    print("Yes")
else:
    print("No")