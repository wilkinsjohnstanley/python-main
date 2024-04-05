class Solution(object):
    def majorityElement(self, nums):
        candidate = None
        count = 0

        # Finding candidate
        for num in nums:
            if count == 0:
                candidate = num
                count = 1
            elif num == candidate:
                count += 1
            else:
                count -= 1

        # Verifying if candidate is majority
        count = 0
        for num in nums:
            if num == candidate:
                count += 1

        if count > len(nums) / 2:
            return candidate
        else:
            return None

    # Example usage:
    nums = [3, 3, 4, 2, 4, 4, 2, 4, 4]
    print("Majority Element:", majority_element(nums))
    
                