def bubble_sort_recursive(collection: list[Any]) -> list[Any]:
    """ It is similar to iterative bubble sort but recursive.
    : param collection: mutable ordered sequence of elements
    : return: the same list in ascending order
    """
  
    length = len(collection)
    swapped = True
    for i in range(length - 1):
        if collection[i] > collection[i + 1]:
            collection[i], collection[i + 1] = collection[i + 1], collection[i]
            swapped = False

    return collection if swapped else bubble_sort_recursive(collection)
