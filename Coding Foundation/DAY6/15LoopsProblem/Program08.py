# reverse an integer 

def main():
    #take user input
    n =  int(input("Enter the number: "))

    rev = 0
    #loops start
    while(n!=0):
        r = n % 10
        rev = rev * 10 + r
        n = int(n / 10)

    print(f"The reverse number is: {rev}")


if __name__ == "__main__":
    main()