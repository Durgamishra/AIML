def findFactorial(n):
    fact = 1
    for i in range(1,n+1):
        fact = fact * i
        i+=1
    return fact
num = int(input("Enter the number: "))
print(f"The factorial of {num} is {findFactorial(num)}")