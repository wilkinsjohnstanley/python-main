def max_sum_subarray(arr, k):
    if k > len(arr):
        return "Window size k is larger than array length"
    
    max_sum = float('-inf')
    window_sum = sum(arr[:k])

    for i in range(len(arr) - k + 1):
        max_sum = max(max_sum, window_sum)
        if i + k < len(arr):
            window_sum = window_sum - arr[i] + arr[i + k]

    return max_sum

# Example usage:
arr = [4, 2, 1, 7, 8, 1, 2, 8, 1, 0]
k = 3
print(max_sum_subarray(arr, k))  # Output: 16 (sum of the subarray [7, 8, 1])
