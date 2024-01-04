def subarray_sum(nums, k):
    count = 0
    sum_dict = {0: 1}
    current_sum = 0

    for num in nums:
        current_sum += num
        if current_sum - k in sum_dict:
            count += sum_dict[current_sum - k]
        sum_dict[current_sum] = sum_dict.get(current_sum, 0) + 1

    return count

# Example usage:
nums = [1, 2, 3, -1, 2]
k = 4
result = subarray_sum(nums, k)
print(result)

#Answer:
2
