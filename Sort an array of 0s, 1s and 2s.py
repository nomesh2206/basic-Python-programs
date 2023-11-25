def sortArray(arr):
    count_0 = 0
    count_1 = 0
    count_2 = 0

    for num in arr:
        if num == 0:
            count_0 += 1
        elif num == 1:
            count_1 += 1
        else:
            count_2 += 1

    for i in range(count_0):
        arr[i] = 0

    for i in range(count_0, count_0 + count_1):
        arr[i] = 1

    for i in range(count_0 + count_1, len(arr)):
        arr[i] = 2


n = 6
arr = [2, 0, 2, 1, 1, 0]
sortArray(arr)
print(arr)

------------------------------------------------------------------
Output:
[0, 0, 1, 1, 2, 2]
