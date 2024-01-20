############ Selection sort in Python  ################
# Selection sort is a sorting algorithm that selects the smallest element from an unsorted list in each iteration
# and places that element at the beginning of the unsorted list.

#Working:
#1. Set the first element as minimum
#2. Compare minimum with the second element. If the second element is smaller than minimum, assign the second element as minimum.
#    Compare minimum with the third element. 
#        Again, if the third element is smaller, then assign minimum to the third element otherwise do nothing. The process goes on until the last element.
#3. After each iteration, minimum is placed in the front of the unsorted list.
#4. For each iteration, indexing starts from the first unsorted element. 
#5. Step 1 to 3 are repeated until all the elements are placed at their correct positions.


def selectionSort(array):
    size = len(array)
    for step in range(size):
        min_idx = step

        for i in range(step + 1, size):
         
            # to sort in descending order, change > to < in this line
            # select the minimum element in each loop
            if array[i] < array[min_idx]:
                min_idx = i
         
        # put min at the correct position
        (array[step], array[min_idx]) = (array[min_idx], array[step])


lst = [-2, 45, 0, 11, -9]
selectionSort(lst)
print('Sorted Array in Ascending Order:')
print(data)
