class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l=[]
        for i in range(0,len(nums)-1):
            for j in range(1,len(nums)):
                if(nums[i]+nums[j]==target):
                    l.extend([i,j])
        return list(set(l))

