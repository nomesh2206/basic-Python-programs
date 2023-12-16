def reverse(arr, n, k):
    i = 0
     
    while(i<n):
        left = i 
 
        # To handle case when k is not multiple of n
        right = min(i + k - 1, n - 1) 
 
        # Reverse the sub-array using left, right pointer
        while (left < right):
             
            arr[left], arr[right] = arr[right], arr[left]
            left+= 1;
            right-=1
        i+= k
