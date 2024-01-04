def max_sum_with_k(a, n, k):
    sum_val, max_val, prv, i, j = 0, 0, 0, 0, 0

    while i < k:
        sum_val += a[i]
        i += 1

    max_val = sum_val

    while i < n:
        sum_val += a[i]
        prv += a[j]
        j += 1
        i += 1
        max_val = max(sum_val, max_val)

        if prv < 0:
            sum_val -= prv
            prv = 0
            max_val = max(sum_val, max_val)

    return max_val

# Example usage:
arr = [1, 2, 3, -10, 5]
size = len(arr)
k_val = 3
result = max_sum_with_k(arr, size, k_val)
print(result)
