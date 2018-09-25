class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        lens=len(nums)
        for i in range(0,lens):
            for j in range(1,lens+1):
                if nums[i]+nums[j]==target:
                    return [i,j]
