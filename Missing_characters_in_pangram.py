def missingPanagram(self, s):
        missing = ""
        alphabet = 'abcdefghijklmnopqrstuvwxyz'
        s = s.lower()
        for letter in alphabet:
            if letter not in s:
                missing += letter
        
        if len(missing) >= 1:
            return missing
        else :
            return -1
