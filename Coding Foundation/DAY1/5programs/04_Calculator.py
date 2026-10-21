num1 = int(input("Enter number 1: "))
num2 = int(input("Enter number 2: "))
opp = input("Enter the operator: ")
match opp:
    case '+':
        print(f"{num1} + {num2} = {num1+num2}")
    case '-' :
        print(f"{num1} + {num2} = {num1-num2}")
    case '*':
        print(f"{num1} + {num2} = {num1*num2}")
    case '/':
        print(f"{num1} + {num2} = {num1/num2}")
    case '%':
        print(f"{num1} + {num2} = {num1%num2}")