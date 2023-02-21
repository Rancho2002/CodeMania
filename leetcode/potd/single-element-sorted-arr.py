from collections import Counter
class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        nums=Counter(nums)
        for i in nums:
            if(nums[i]==1):
                return i

'''
from functools import reduce
class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        return reduce(lambda x,y:x^y, nums)
             
'''