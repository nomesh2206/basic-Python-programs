class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        ptr1 = 0
        ptr2 = 0
        for i in s:
            if ptr2 == len(t):
                return 0
            if i == t[ptr2]:
                ptr2 += 1
                ptr1 += 1
        return len(t) - ptr1
