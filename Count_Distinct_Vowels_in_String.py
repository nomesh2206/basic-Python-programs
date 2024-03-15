
    def countVowels(self,s):
        #code here
        vowels = "aeiouAEIOU"
        distinct_vowels = set()
        for char in s:
            if char in vowels:
                distinct_vowels.add(char.lower())
        return len(distinct_vowels)
