def maxLength(arr):
    # To store the answer
    ans = 0
 
    # Find all subarrays
    for i in range(len(arr)):
        # To store the length of subarray
        length = 0
        for j in range(i, len(arr)):
            # Increment the length
            length += 1
 
            # Boolean variable to tell whether the sum 
            # of all elements is even or not
            val = False
 
            # To store the sum of all elements of subarray
            subarray_sum = 0
 
            for k in range(i, j + 1):
                subarray_sum += arr[k]
 
            # When the sum of all elements is even
            if subarray_sum % 2 == 0:
                ans = max(ans, length)
 
    return ans
 
# Driver Code
arr = [1, 2, 3, 2]
print(maxLength(arr))
