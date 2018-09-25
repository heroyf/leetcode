class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        lens=len(nums)
        for i in range(lens):
            j=nums[i]
            if target-j in nums and i != nums.index(target-j):
                return (i,nums.index(target-j))
