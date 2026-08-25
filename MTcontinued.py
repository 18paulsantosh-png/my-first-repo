while True:
    n = int(input("Enter a number(1-1000): "))

    if n > 0 and n <= 1000:
        print("Multiplication table of", n)
        for i in range(1, 11):
            print(n, "x", i, "=", n * i)
    else:
        print("Please enter a number between 1 and 1000")

    choice = input("Do you want to continue?(y/n): ")
    if choice == "n" or choice == "N":
        break