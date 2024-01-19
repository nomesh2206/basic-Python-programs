def bubble_sort(array):
    n = len(array)
    for i in range(n):
        already_sorted = True
       
        for j in range(n - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]

                already_sorted = False

        if already_sorted:
            break

    return array

Steps-to-Follow:
# Create a flag that will allow the function to terminate if the array is sorted.
# Start looking at each item of the list one by one, comparing it with its adjacent value. 
# With each iteration, the portion of the array that you look at shrinks because the remaining items have already been sorted.
# If the item you're looking at is greater than its adjacent value, then swap them
# Since you had to swap two elements, set the `already_sorted` flag to `False` so the algorithm doesn't finish prematurely

