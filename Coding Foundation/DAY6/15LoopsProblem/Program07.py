def main():
    #calculate the no of digits in a number
    
    #digit input 
    n = int(input("Enter the number to find its no of digits: "))

    #count
    count = 0

    while(n != 0):
        count = count +1
        n = n//10

    print(count) 
    return

if __name__ == "__main__":
    main()