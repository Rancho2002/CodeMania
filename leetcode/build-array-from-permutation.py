class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        l=[]
        for i in range(len(nums)):
            l.append(nums[nums[i]])
        return l
'''
https://leetcode.com/problems/build-array-from-permutation/submissions/
Runtime: 318 ms, faster than 17.46% of Python3 online submissions for Build Array from Permutation.
Memory Usage: 14 MB, less than 89.88% of Python3 online submissions for Build Array from Permutation.
'''