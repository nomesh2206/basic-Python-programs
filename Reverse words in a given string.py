class Solution:
    # Function to reverse words in a given string.
    def reverseWords(self, S):
        # code here
        words = S.split(".")
        ans = []
        
        for i in range(len(words)-1, -1, -1):
            ans.append(words[i])
            if i > 0:
                ans.append(".")
        
        return ''.join(ans)

# Example usage:
# solution = Solution()
# result = solution.reverseWords("Hello.World")
# print(result)

#Output:"World.Hello"
