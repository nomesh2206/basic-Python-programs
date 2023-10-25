"""
Created on Wed Oct 25 15:50:32 2023
@author: nomesh
"""
nested_dict = {'a':1, 'b':3, 'c':{'x':2, 'y':4, 'z':6}, 'd':{'m':8, 'n':10}, 'e':5}

def flatten_dict(nested_dict, parent_key='', sep='_'):
    flattened_dict = {}
    for key, value in nested_dict.items():
        new_key = f"{parent_key}{sep}{key}" if parent_key else key
        if isinstance(value, dict):
            flattened_dict.update(flatten_dict(value, new_key, sep=sep))
        else:
            flattened_dict[new_key] = value
    return flattened_dict

flattened_dict = flatten_dict(nested_dict)
print(flattened_dict)

Output:
{'a': 1, 'b': 3, 'c_x': 2, 'c_y': 4, 'c_z': 6, 'd_m': 8, 'd_n': 10, 'e': 5}
