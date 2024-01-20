#Insertion sort is a sorting algorithm that places an unsorted element at its suitable place in each iteration.
#Insertion sort works similarly as we sort cards in our hand in a card game.
#We assume that the first card is already sorted then, we select an unsorted card. If the unsorted card is greater than the card in hand, 
#it is placed on the right otherwise, to the left. In the same way, other unsorted cards are taken and put in their right place.
#A similar approach is used by insertion sort.

def insertion_sort(array):
   
    for i in range(1, len(array)):
        # This is the element we want to position in its correct place
        key_item = array[i]

        # Initialize the variable that will be used to find the correct position of the element referenced by `key_item`
        j = i - 1

        # Run through the list of items (the left portion of the array) and find the correct position
        # of the element referenced by `key_item`. Do this only
        # if `key_item` is smaller than its adjacent values.
        while j >= 0 and array[j] > key_item:
            # Shift the value one position to the left and reposition j to point to the next element (from right to left)
            array[j + 1] = array[j]
            j -= 1

        # When you finish shifting the elements, you can position`key_item` in its correct location
        array[j + 1] = key_item

    return array

