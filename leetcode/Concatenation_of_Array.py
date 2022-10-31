class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        l=[]
        for i in range(len(nums)):
            l.append(nums[i])   
        for i in range(len(nums)):
            l.append(nums[i]) 
        return l

'''
https://leetcode.com/problems/concatenation-of-array/
Runtime: 125 ms, faster than 76.08% of Python3 online submissions for Concatenation of Array.
Memory Usage: 14.3 MB, less than 25.45% of Python3 online submissions for Concatenation of Array.
'''