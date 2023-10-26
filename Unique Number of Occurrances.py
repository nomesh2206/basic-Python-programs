Given an array of integers arr, return true if the number of occurrences of each value in the array is unique or false otherwise.

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        list=[]
        s = set()
        occurance = Counter(arr)
        for value in occurance.values():
            list.append(value)

        for x in list:
            if x in s:
                return False
            s.add(x)
        return True
