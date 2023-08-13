'''
#! log(num,base) this result can tell what is the maximum possible power of any number 
for eg.
if num = 27
log(27,3)= 3 that mean for number 3 the highest possible power is 3
'''

from math import log

class Solution:
	# @param A : integer
	# @return an integer
    def isPower(self, A):
        if A==1: return 1
        elif A<4: return 0
        
        
        for i in range(2,int(A**0.5)+1):
            for j in range(2,int(log(A,i))+1):
                if i**j ==A:
                    return 1
        return 0