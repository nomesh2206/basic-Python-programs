rows = int(input("enter Diamond pattern rows = "))

for i in range(1, rows+1):
    for j in range(1, rows-i+1):
        print(end = ' ')
        
    for k in range(1, 2*i):
        print(k, end='')
    
    print()
    
for i in range(1, rows):
    for j in range(1, i+1):
        print(end = ' ')
    
    for k in range(1, (2*(rows-i))):
        print(k, end = '')
    
    print()

-------------------------------------------------------------
Output:
enter Diamond pattern rows = 5
    1
   123
  12345
 1234567
123456789
 1234567
  12345
   123
    1
