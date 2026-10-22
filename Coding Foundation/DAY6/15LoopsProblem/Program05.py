def main():
    #multiplication table
    n = int( input( "Enter the number to print its table: "))
    for i in range(1,11):
        print(f"{n} * {i} = {n*i}")
    return

if __name__ == "__main__":
    main()