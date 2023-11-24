rows = int(input("enter Diamond pattern rows = "))

for i in range(1, rows+1):
    for j in range(1, rows-i+1):
        print(end = ' ')
        
    for k in range(1, 2*i):
        if k == 1 or k == 2*i-1:
            print(k, end='')
        else:
            if i == rows:
                print(k, end='')
            else:
                print(' ', end='')
    
    print()
    
for i in range(1, rows):
    for j in range(1, i+1):
        print(end = ' ')
    
    for k in range(1, (2*(rows-i))):
        if k == 1 or k == (2*(rows-i))-1:
            print(k, end='')
        else:
            print(' ', end='')
    
    print()

-------------------------------------------------------------

Output:
enter Diamond pattern rows = 5
    1
   1 3
  1   5
 1     7
123456789
 1     7
  1   5
   1 3
    1
