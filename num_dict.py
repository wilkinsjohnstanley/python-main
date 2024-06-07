'''One-Pass Hash Table'''
# class Solution:
#     def twoSum(self, nums, target):
#         num_dict = {}
#         for i, num in enumerate(nums):
#             complement = target - num
#             if complement in num_dict:
#                 return [num_dict[complement], i]
#             num_dict[num] = i
#         return None
'''Brute O(n^2)'''
class Solution(object):
  def twoSum(self, nums, target):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
    return []
'''Two-Pass Hash Table O(n)'''
# class Solution(object):
#   def twoSum(self, nums, target):
#     numMap = {}
#     for i, num in enumerate(nums):
#         numMap[num] = i
#     for i, num in enumerate(nums):
#         complement = target - num
#         if complement in numMap and numMap[complement] != i:
#             return [i, numMap[complement]]
#     return []

# Example usage
nums = [1, 2, 3]
target = 5
solution = Solution()
result = solution.twoSum(nums, target)
print(result)  # Output: [1, 2]
