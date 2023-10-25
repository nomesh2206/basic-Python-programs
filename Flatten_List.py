"""
Created on Wed Oct 25 16:01:20 2023
@author: nomesh
"""

def flatten_list(nested_list):
    flattened_list = []
    for item in nested_list:
        if isinstance(item, list):
            flattened_list.extend(flatten_list(item))
        else:
            flattened_list.append(item)
    return flattened_list

# Example nested list
nested_list = [1, [2, [3, 4]], 5, [6, 7, [8, 9]]]

flattened_list = flatten_list(nested_list)
print(flattened_list)

Output:
[1, 2, 3, 4, 5, 6, 7, 8, 9]
