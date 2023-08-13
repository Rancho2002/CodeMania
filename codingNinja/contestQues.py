def ninjaAndStringConversion(n: int, s: str) -> str:
    # write your code here
    ans=""
    for i in range(len(s)):
        if ord(s[i])>=65 and ord(s[i])<=65+26:
            code=ord(s[i])-1 if ord(s[i])-1!=64 else ord('Z')
        else:
            code=(ord(s[i])+1) if ord(s[i])+1!=123 else ord('a')
        
        ans+=chr(code)
    
    return ans


ninjaAndStringConversion(3,'Pqr')