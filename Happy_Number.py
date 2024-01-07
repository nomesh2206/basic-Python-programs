def sumOfDigit(n):
    res = 0
    rem = 0 
    while n>0:
        rem = n%10
        res = res + rem*rem
        n = n//10
    return res

n = int(input("enter the number : "))
result = n
while result!=1 and result!=4:
    result = sumOfDigit(result)
    
if result==1:
    print(n," is a happy number.")
else:
    print(n, " is not a happy number.")
