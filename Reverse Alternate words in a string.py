s = input("Enter a String")
s = s.split()
def rev(string):
  string = string[::-1]
  return string
r = ""
for i in range(len(s)):
  if i%2 == 0:
    r += rev(s[i]) + " "
  else:
    r += s[i] + " "
print("String after reversal", r)
    
