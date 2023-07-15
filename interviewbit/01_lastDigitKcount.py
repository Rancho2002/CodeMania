class Solution:
    #@param A : integer
    #@param B : integer
    #@param C : integer
    #@return an integer
    def solve(self, A, B, C):
        
        while(A<=B and A%10!=C):
            A+=1
        
        if(A>B): return 0
        
        num=(B-A)//10 +1
        
        return num