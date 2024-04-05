class Solution(object):
    def max_subarray(self, nums):
        max_so_far = max_ending_here = nums[0]
        for num in nums[1:]:
            max_ending_here=max(num, max_ending_here+num)
            max_so_far=max(max_so_far, max_ending_here)
        return max_so_far
solution = Solution()
nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print("Maximum subarray sum:", solution.max_subarray(nums))
        