input = input("Enter a string to un-ROT2.")

str1 = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
str2 = "CDEFGHIJKLMNOPQRSTUVWXYZABcdefghijklmnopqrstuvwxyzab"

t = str.maketrans(str1, str2)

print (input.translate(t))

-------------------------------------------------------------------

