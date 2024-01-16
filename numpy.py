##Create 1-d Numpy Array
lst = [1,2,3,4,5]
arr = np.array(lst)
print(arr)

##Create n-d Numpy Array
a = np.random.randint(1,12,(6,5))
print(a)

##Sorting Numpy array
np.sort(a)  --> (for nd-array, it will sort row-wise)

np.sort(a,axis=0)  --> (for nd-array, it will sort column-wise)
