#

#! Wrong sol
def minSteps(str : str) -> int:
    # code here
    ans=0
    val=ord(str[0])
    for i in str:
        if(ord(i)^val!=0):
            val=ord(i)
            ans+=1
    return ans

print(minSteps("bbaaabb"))