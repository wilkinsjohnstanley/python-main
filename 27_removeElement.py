# class Solution(object):
#     def removeElement(self, nums, val):
#         for num in range(len(nums)):
#             if num == val:
#                 nums.remove(num)
#             else:
#                 notVal+=1
#         return nums, notVal

# class Solution(object):
#     def removeElement(nums, val):
#     j = 0
#     for i in range(len(nums)):
#         if nums[i] != val:
#             nums[j] = nums[i]
#             j += 1
#     return j
'''Accepted answer'''
''' Two pointers; One Array. 
Overwrite indexes with values that aren't the specified one.
If the value is acceptable, overwrite it over the beginning of the array.
'''
class Solution(object):
    @staticmethod
    def removeElement(nums, val):
        '''a pointer to keep track of the current valid elements in the array.'''
        j = 0
        for i in range(len(nums)):
            '''if the current element is not val'''
            if nums[i] != val:
                '''
                assigns the value of the current value nums[i] 
                to the position nums[j], which is index 0. 
                This effectively removes the value val 
                by overwriting it with a valid element
                '''
                nums[j] = nums[i]
                #move to the next position where a valid element should be placed.
                j += 1
        return j

# Usage
nums = [3, 2, 2, 3]
val = 3
new_length = Solution.removeElement(nums, val)

print("New Length:", new_length)  # This should print the new length of the array after removing the element
print("Updated nums:", nums[:new_length])  # This prints the updated nums list containing only the valid elements
'''We use list slicing (nums[:new_length]) to print 
only the elements up to the new length, 
as the remaining elements may contain garbage values. '''