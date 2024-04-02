class Solution(object):
    def containsDuplicate(self, nums):
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] == nums[j]:
                    return True
        return False

# Instantiate Solution class
sol = Solution()
nums = [1, 2, 3, 1]
print(sol.containsDuplicate(nums))
