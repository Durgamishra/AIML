def main():

    #factorial of a number
    n = int(input("Enter the number to find its factorial: "))

    fact = 1

    #loop for calculating factorial of a number
    for i in range(n,0,-1):
        fact = fact * i

    print(fact)

    return

if __name__ == "__main__":
    main()