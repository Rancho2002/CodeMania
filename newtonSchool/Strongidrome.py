# Your code here
def isPalindrome(s):
    for i in range(len(s)//2):
        if(s[i]==s[-1+i]):
            return True
    return False

def isN_1(s):
    n=len(s)
    s=s[:n//2]
    for i in range(len(s)):
        if(s[i]==s[-1+i]):
            return True
    return False

def isN_3(s):
    n=len(s)
    s=s[(n+3-1)//2:]
    for i in range(len(s)):
        if(s[i]==s[-1+i]):
            return True
    return False


n=input()
# print(isPalindrome(n))
# print(isN_1(n))
# print(isN_3(n))
if(isPalindrome(n) and isN_1(n) and isN_3(n)):
    print("Yes")
else:
    print("No")