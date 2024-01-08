class Solution:
    def uniqueOccurrences(self, arr):
        hm = {}

        for num in arr:
            if num in hm:
                hm[num] += 1
            else:
                hm[num] = 1

        occurrences_set = set()
        for key in hm:
            if hm[key] in occurrences_set:
                return False
            else:
                occurrences_set.add(hm[key])

        return True
