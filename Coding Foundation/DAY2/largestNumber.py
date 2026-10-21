def findLargest(a,b,c):
    if(a>b and a>c):
        return (f"{a}")
    elif (b>a and b>c):
        return (f"{b}")
    else:
        return(f"{c}")

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
num3 = int(input("Enter the last number "))

print(f"comparing {num1}, {num2}, {num3} the largest number is {findLargest(num1,num2,num3)}")