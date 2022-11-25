class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        su=0
        pro=1
        while(n>0):
            a=n%10
            n=int(n/10)
            su=su+a
            pro=pro*a
        return pro-sus