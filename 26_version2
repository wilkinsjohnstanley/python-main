def removeDuplicates(self, nums):
    j = 1
    for i in range(1, len(nums)):
        if nums[i] != nums[i - 1]:
            nums[j] = nums[i]
            j += 1
    return j
    
nums = [1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 6]
print("Original Array:", nums)
new_length = removeDuplicates(nums)
print("Modified Array:", nums[:new_length])
print("New Length:", new_length)
