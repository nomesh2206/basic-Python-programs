# -*- coding: utf-8 -*-
"""
Created on Mon Nov 27 13:34:55 2023

@author: 
    """
    
    
def generate_pascals_triangle(n):
    triangle = []

    for i in range(n):
        row = [1] * (i + 1)

        for j in range(1, i):
            row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]

        triangle.append(row)

    return triangle

def print_pascals_triangle(triangle):
    for row in triangle:
        print(" ".join(map(str, row)))

# Example: Print the first 5 rows of Pascal's Triangle
num_rows = 5
pascals_triangle = generate_pascals_triangle(num_rows)
print_pascals_triangle(pascals_triangle)
