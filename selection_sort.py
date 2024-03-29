def selection_sort(arr):
    n = len(arr)
    # Traverse through all array elements
    for i in range(n):
        # Find the minimum element in the unsorted part of array
        min_index = i
        '''find the index of the minimum element in the unsorted part of the array'''
#This loop iterates through the elements of the array starting from i + 1. 
#i represents the index of the first unsorted element, 
#and i + 1 ensures that we're considering only the unsorted part of the array.
        for j in range(i + 1, n):
#This condition checks if the element at index j is less than the element at 
#the current minimum index (min_index). If it is, then j becomes the new minimum index.
            if arr[j] < arr[min_index]:
                min_index = j
        
        # Swap the found minimum element with the first element
        arr[i], arr[min_index] = arr[min_index], arr[i]

# Example usage:
arr = [64, 25, 12, 22, 11]
selection_sort(arr)
print("Sorted array is:", arr)
