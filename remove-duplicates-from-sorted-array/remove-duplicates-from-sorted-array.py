class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        j = 1
        n = len(nums)
        for i in range(1, n):
            if nums[i - 1] < nums[i] :
                nums[j] = nums[i]
                j += 1
        return j
        