def checkEvenOrOdd(num):
    if(num%2==0):
        return "Even"
    else:
        return "Odd"
num = int(input("enter the number to check even or odd: "))
print(checkEvenOrOdd(num))