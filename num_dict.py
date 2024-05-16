class Solution:
    def twoSum(self, nums, target):
        num_dict = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in num_dict:
                return [num_dict[complement], i]
            num_dict[num] = i
        return None

# Example usage
nums = [1, 2, 3]
target = 5
solution = Solution()
result = solution.twoSum(nums, target)
print(result)  # Output: [1, 2]
