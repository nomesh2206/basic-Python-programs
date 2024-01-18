def pattern(n):
    for i in range(n):
        for j in range(i+1):
            x = 0
            for k in range(j):
                x = x+n-k
            if j%2 == 0:
                print(x+i-j+1, end=" ")
            else:
                print(x+n-i, end=" ")
        print()

pattern(5)    

'''Pattern:
 1 
 2 9 
 3 8 10 
 4 7 11 14 
 5 6 12 13 15
'''    
