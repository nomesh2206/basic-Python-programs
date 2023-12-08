def merge(list_1: List[int], list_2: List[int]):
    x = len(list_1)
    y = len(list_2)
    i, j, k = x-1, y-1, x+y-1
    
    list_1.extend([0] * y)

    while j >= 0:
        print("i =", i, "j =", j)
        if i >= 0 and list_1[i] >= list_2[j]:
            list_1[k] = list_1[i]
            i -= 1
            
        else:
            list_1[k] = list_2[j]
            j -= 1
            
        k -= 1
        print(k)

        
        
list_1 = [1, 3, 5, 7, 9, 11, 13, 15]
list_2 = [0,10]
merge(list_1, list_2)
print(list_1)
