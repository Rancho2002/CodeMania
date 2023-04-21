class Solution:
    ##Complete this function
    # Function to check if given number n is a power of two.
    def isPowerofTwo(self,n):
        ##Your code here
        s=0
        e=62
        m=(s+e)//2
        while(s<=e):
            if(2**m==n):
                return True
            elif(2**m<n):
                s=m+1
            else:
                e=m-1
            m=(s+e)//2
        
        return False            
    