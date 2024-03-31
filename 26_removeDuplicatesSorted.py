def removeDuplicates(nums):
    if not nums:
        return 0

    # Initialize pointer for the unique elements
    unique_ptr = 0

    # Iterate through the array
    for i in range(1, len(nums)):
        # If the current element is different from the previous one,
        # increment the unique pointer and assign the current element
        # to the position pointed by the unique pointer
        if nums[i] != nums[unique_ptr]:
            unique_ptr += 1
            nums[unique_ptr] = nums[i]

    # The unique_ptr will be at the index of the last unique element,
    # so the length of the modified array will be unique_ptr + 1
    return unique_ptr + 1

# Example usage:
nums = [1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 6]
print("Original Array:", nums)
new_length = removeDuplicates(nums)
print("Modified Array:", nums[:new_length])
print("New Length:", new_length)
